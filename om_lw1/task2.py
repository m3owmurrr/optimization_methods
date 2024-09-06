# Метод золотого сечения
# вывести функцию, минимум, интервал неопределнности, функция в точке, сходимость, N - индек неопредленности
import numpy as np
import matplotlib.pyplot as mpl

f = lambda x: x ** 2 - 6 * x + 12
# f = lambda x: 2*(x**2) - 12*x + 19

a, b = 1, 11  # (a, b)
k = 0
eps = 0.5

y = a + ((3 - 5 ** (1 / 2)) / 2) * (b - a)
z = a + b - y
while (abs(b - a) > 2*eps):
    print(f'k={k}: y={y} z={z} f(y)={f(y)}   f(z)={f(z)} ')
    if (f(y) <= f(z)):
        b = z
        z = y
        y = a + b - y
    else:
        a = y
        y = z
        z = a + b - z
    k += 1
    print(f'k={k}: y={y} z={z} L{k}={a, b}\n')



minX = (a + b) / 2
print('===== ANSWER =====')
print(f'f(x)=x^2 - 6x + 12\nminX={minX}   min(f)={f(minX)}\nL{k}={a, b}\nСходимость: {((1 - (3-5**(1/2))/2))**(k+1) }')

x = np.arange(1, 11, 0.1)
mpl.plot(x, f(x))
mpl.scatter(minX,f(minX))
mpl.show()