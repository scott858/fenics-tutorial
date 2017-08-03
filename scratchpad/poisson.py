import fenics as fe
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
# matplotlib.interactive(True)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == "__main__":

    mesh = fe.UnitSquareMesh(8, 8)
    V = fe.FunctionSpace(mesh, 'P', 1)

    u_D = fe.Expression('1 + x[0]*x[0] + 2*x[1]*x[1]', degree=2)


    def boundary(x, on_boundary):
        return on_boundary


    bc = fe.DirichletBC(V, u_D, boundary)

    u = fe.TrialFunction(V)
    v = fe.TestFunction(V)
    f = fe.Constant(-6.0)
    a = fe.dot(fe.grad(u), fe.grad(v)) * fe.dx
    L = f * v * fe.dx

    u = fe.Function(V)
    fe.solve(a == L, u, bc)

    vtk_file = fe.File('poisson/solution.pvd')
    vtk_file << u

    error_L2 = fe.errornorm(u_D, u, 'L2')

    vertex_values_u_D = u_D.compute_vertex_values(mesh)
    vertex_values_u = u.compute_vertex_values(mesh)

    error_max = np.max(np.abs(vertex_values_u_D - vertex_values_u))

    print('error_L2 =', error_L2)
    print('error_max=', error_max)

    # fe.plot(u)
    # fe.plot(mesh)
    X = np.arange(0, 1, .01)
    Y = np.arange(0, 1, .01)
    X, Y = np.meshgrid(X, Y)


    @np.vectorize
    def func(x, y):
        return u(x, y)


    Z = func(X, Y)

    fig = plt.figure()
    ax = fig.gca(projection="3d")
    surf = ax.plot_surface(X, Y, Z,
                           cmap=plt.cm.coolwarm,
                           linewidth=0,
                           antialiased=False)

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
