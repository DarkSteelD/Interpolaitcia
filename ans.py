from scipy import integrate
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols, lambdify
with open('5.txt', 'r') as f:
    str = f.readline()
    fun =  parse_expr(str)
    a = float(f.readline())
    b = float(f.readline())
    n = int(f.readline())
nodes_y = []
x = symbols("x")
for i in range(0,7):
    nodes_y.append(a+(b-a)/6*i)
fun_callable = lambdify(x, fun, 'numpy')
exact_integral = integrate.quad(fun_callable, a, b)[0]
h = (b-a)/6
ans_y = h/3*(fun.subs(x,nodes_y[0])+4*fun.subs(x,nodes_y[1])+2*fun.subs(x,nodes_y[2])+4*fun.subs(x,nodes_y[3])+2*fun.subs(x,nodes_y[4])+4*fun.subs(x,nodes_y[5])+fun.subs(x,nodes_y[6]))
with open('результат.txt', 'w') as file:
    file.write(f"Точное значение интеграла: {exact_integral}")
    file.write(f"Численное значение интеграла: {ans_y} ")
    file.write(f"Отличие: {abs(exact_integral - ans_y)} ")

