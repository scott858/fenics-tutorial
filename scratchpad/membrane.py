import fenics as fe
import numpy as np
import mshr
import matplotlib
matplotlib.use('Qt5Agg')
# matplotlib.interactive(True)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == "__main__":
    domain = mshr.Circle(fe.Point(0, 0), 1)
    mesh = mshr.generate_mesh(domain, 64)

    beta = 8
    R0 = 0.6
    p = fe.Expression(
        '4*exp(-pow(beta, 2)*(pow(x[0], 2) + pow(x[1] - R0, 2)))',
        degree=1, beta=beta, R0=R0
    )

    V = fe.FunctionSpace(mesh, 'P', 1)
    w = fe.TrialFunction(V)
    v = fe.TestFunction(V)
    a = fe.dot(fe.grad(w), fe.grad(v)) * fe.dx
    L = p * v * fe.dx
    w = fe.Function(V)


    def boundary(x, on_boundary):
        return on_boundary


    bc = fe.DirichletBC(V, 0, boundary)
    fe.solve(a == L, w, bc)
    p = fe.interpolate(p, V)

    vtkfile_w = fe.File('poisson_membrane/deflection.pvd')
    vtkfile_w << w
    vtkfile_p = fe.File('poisson_membrane/load.pvd')
    vtkfile_p << p

    # fe.plot(w, title="Deflection")
    # plt.figure()
    # fe.plot(p, title="Load")
    # plt.show()
    X = np.arange(0, 1, .01)
    Y = np.arange(0, 1, .01)
    X, Y = np.meshgrid(X, Y)


    @np.vectorize
    def func(x, y):
        if x**2 + y**2 < 1:
            return w(x, y)
        else:
            return 0


    Z = func(X, Y)

    fig = plt.figure()
    ax = fig.gca(projection="3d")
    surf = ax.plot_surface(X, Y, Z,
                           cmap=plt.cm.coolwarm,
                           linewidth=0,
                           antialiased=False)

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
