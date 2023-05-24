from sympy import pprint, Integral, Symbol
x = Symbol('x')
k = Symbol('k')
F = Integral(k*x, x).doit()
pprint(F)