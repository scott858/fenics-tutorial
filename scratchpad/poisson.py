import fenics as fe

mesh = fe.UnitSquareMesh(8, 8)
V = fe.FunctionSpace(mesh, 'P', 1)

u_D = fe.Expression('1 + x[0]*x[0] + 2*x[1]*x[1]', degree=2)
