import sympy
import math

def cau3b_2274802010306():
    x = sympy.Symbol("x")
    y = sympy.Symbol("y")
    dy = x*y**2
    dx = (x * sympy.exp(x) - 2) / sympy.sqrt(x**2 - 4*x + 5)
    fy = sympy.Integral(dy, (y, 1, 20)).doit().evalf()
    print(fy)
    fx = sympy.Integral(dx, (x,0,1)).doit().evalf()
    print(fx)
cau3b_2274802010306()