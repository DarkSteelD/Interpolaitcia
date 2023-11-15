from scipy import integrate
import numpy as np
def f(x):
    return x**2
a = float(input("Введите начальную точку отрезка: "))
b = float(input("Введите конечную точку отрезка: "))
n = int(input("Введите количество узлов (целое число): "))
x_nodes = np.linspace(a, b, n)
exact_integral = integrate.quad(f, a, b)[0]
numerical_integral = np.sum(f(x_nodes)) * (b - a) / n
with open('результат.txt', 'w') as file:
    file.write(f"Точное значение интеграла: {exact_integral}")
    file.write(f"Численное значение интеграла: {numerical_integral} ")
    file.write(f"Отличие: {abs(exact_integral - numerical_integral)} ")

