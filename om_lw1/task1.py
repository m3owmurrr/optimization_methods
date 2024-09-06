# dichotomy method
# вывести функцию, минимум, интервал неопределнности, функция в точке, сходимость, N - индек неопредленности
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x ** 2 - 6 * x + 12
# f = lambda x: 2*(x**2) - 12*x + 19

a, b = 1, 11  # (a, b)
k = 0
delta = 0.2
eps = 0.5
while (abs(b - a) > 2*eps):
    y = round(((a + b - delta) / 2), 5)
    z = round(((a + b + delta) / 2), 5)
    if (f(y) <= f(z)):
        b = z
    else:
        a = y
    print(f'k={k}: y={y} z={z}\nf(y)={f(y)}   f(z)={f(z)}   L{2 * (k+1)}={a, b}\n')
    k += 1
minX = (a + b) / 2
print('===== ANSWER =====')
print(f'f(x)=x^2 - 6x + 12\nminX={minX}   min(f)={f(minX)}\nL{2 * k}={a, b}\nСходимость: {1 / (2 ** (k))}')

# Построение графика функции
x = np.arange(0, 10, 0.1)
plt.plot(x, f(x))
plt.scatter(minX, f(minX))

# Установка большего количества делений на осях
plt.xticks(np.arange(0, 10, 1))  # Задаем деления по оси x от -4 до 7 с шагом 1

# Отображение графика
plt.show()