import math
import sympy
from sympy import diff, sqrt
from sympy.abc import x,y,z
import matplotlib.pyplot as plt


#CÂU 1:
def cau1a_2274802010306():
    x = sympy.Symbol('x')
    de_1a = (sympy.sin(x) / 2 * x)
    result_1a = sympy.limit(de_1a, x, (math.pi/2))
    return(result_1a)
print(f"Cau 1a: {cau1a_2274802010306()}")

def cau1b_2274802010306():
    x = sympy.Symbol('x')
    de_1b = ((math.sqrt(x**2 - 2*x + 3)) / (x + 1))
    result_1b = sympy.limit(de_1b, x, 1)
    return(result_1b)
print(f"Cau 1b: {cau1b_2274802010306()}")

#CÂU 2:
def cau2a_2274802010306():
    n = sympy.symbols("n")
    result_2a = sympy.limit_seq(sympy.Sum((2*n + 1)/ (n**2 * (n + 1)), (n, 1, math.inf)).doit())
    print(result_2a)

cau2a_2274802010306()

def cau2b_2274802010306():
    n = sympy.symbols("n")
    result_2b = sympy.limit_seq(sympy.Sum(n / (2*n + 1), (n, 1 , math.inf)).doit())
    print(result_2b)

cau2b_2274802010306()

#CÂU 3:
def cau3a_2274802010306():
    x = sympy.symbols("x")
    fx = (1 - x*sympy.sin(x)) * sympy.sqrt(x**2 - 2*x +3)
    f = sympy.Integral(fx,(x, 0, 1)).doit()
    print(f)
cau3a_2274802010306()


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

# #CÂU 4: 
def cau4_2274802010306():
    p = sqrt(x**2 + y**2 + z**2 - 6*x - 2*y - 2*z + 11)
    f = x**2 + y**2 + (z-1) - 9
    grad_p = sympy.Matrix([diff(p,i) for i in [x,y,z]])
    grad_f = sympy.Matrix([diff(f,i) for i in [x,y,z]])
    solutions = sympy.solve(grad_p.row_join(grad_f), [x,y,z])
    print(solutions)

cau4_2274802010306()

#CÂU 5: 
def cau5_2274802010306():
    time=[1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]
    C=[18, 24, 43, 50, 28, 31, 29, 36, 27, 66, 11, 48]
    from pylab import plot, show
    plot(time, C)
    show()
cau5_2274802010306()