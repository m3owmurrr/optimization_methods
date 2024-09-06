# метод Фибоначчи
# вывести функцию, минимум, интервал неопределнности, функция в точке, сходимость, N - индек неопредленности
import numpy as np
import matplotlib.pyplot as mpl

f = lambda x: x ** 2 - 6 * x + 12
# f = lambda x: 2*(x**2) - 12*x + 19
fibonacci = lambda n: 1 if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

a, b = 1, 11  # (a, b)
k = 0
n = 0
eps = 0.5

while (fibonacci(n) < (b - a) / (2*eps)):
    n += 1
print(n, fibonacci(n))

y = b - (b - a) * (fibonacci(n - 1) / fibonacci(n))
z = a + (b - a) * (fibonacci(n - 1) / fibonacci(n))

while ((abs(b - a) > 2*eps) and (n != 1)):
    print(f'k={k}: y={y} z={z} f(y)={f(y)}   f(z)={f(z)} ')
    n -= 1
    if (f(y) < f(z)):
        b = z
        z = y
        y = b - (b - a) * (fibonacci(n - 1) / fibonacci(n))
    else:
        a = y
        y = z
        z = a + (b - a) * (fibonacci(n - 1) / fibonacci(n))
    k += 1
    print(f'k={k}: y={y} z={z} L{k}={a, b}\n')


minX = (a + b) / 2

print('===== ANSWER =====')
print(f'f(x)=x^2 - 6x + 12\nminX={minX}   min(f)={f(minX)}\nL{k}={a, b}\nСходимость: {1 / (fibonacci(6))}')

x = np.arange(0, 10, 0.1)
mpl.plot(x, f(x))
mpl.scatter(minX,f(minX))
mpl.show()