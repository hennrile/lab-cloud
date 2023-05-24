from sympy import Symbol, exp, sqrt, pi, Integral, pprint
x = Symbol('x')
p = exp(-(x - 10)**2/2)/sqrt(2*pi)
F =Integral(p, (x, 11, 12)).doit().evalf() 
pprint(F)