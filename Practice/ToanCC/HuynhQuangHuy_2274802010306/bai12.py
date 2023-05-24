from sympy import Integral, Symbol, pprint
x = Symbol('x')
F=Integral(x, (x, 2, 4)).doit() 
pprint(F)