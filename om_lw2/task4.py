import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# f = lambda x, y: 6 * (x ** 2) + y ** 2 - x * y + x
f = lambda x, y: 3 * (x ** 2) + 4 * (y ** 2) - 2 * x * y + x
class Point:
    def __init__(self, x, y, f = f):
        self.x = x
        self.y = y
        self.f = f

    def __str__(self):
        return f"({self.x}, {self.y})"

    def f_diffX(self):
        x, y = sp.symbols('x, y')
        f_sym = sp.lambdify((x, y), self.f(x, y))
        return sp.diff(f_sym(x, y), x).subs({x: self.x, y: self.y})

    def f_diffY(self):
        x, y = sp.symbols('x, y')
        f_sym = sp.lambdify((x, y), self.f(x, y))
        return sp.diff(f_sym(x, y), y).subs({x: self.x, y: self.y})

    def gradient(self):
        return Point(self.f_diffX(), self.f_diffY())

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    def norm2(self, p):
        return math.sqrt((p.x-self.x)**2 + (p.y-self.y)**2)

    def tk(self, d):
        return (-1 * d[0]*(self.f_diffX()) - d[1]*(self.f_diffY())) / (6 * (d[0] ** 2) - 4 * d[0] * d[1] + 8 * (d[1] ** 2))

    def np_point(self):
        return np.array([self.x, self.y])

    def point_add(self, arr):
        return Point(self.x + arr[0], self.y + arr[1])

def visual_2d():
    x_range = np.linspace(-2.5, 2.5, 150)
    y_range = np.linspace(-2.5, 2.5, 150)
    X, Y = np.meshgrid(x_range, y_range)
    Z = 6 * X ** 2 + Y ** 2 - X * Y + X

    plt.figure()
    plt.contour(X, Y, Z, levels=20)
    plt.plot([v.x for k, v in x.items()], [v.y for k, v in x.items()], '-o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Метод Флетчера-Ривса')
    plt.grid(True)
    plt.show()

def visual_3d():
    x_range = np.linspace(-2.5, 2.5, 150)
    y_range = np.linspace(-2.5, 2.5, 150)
    X, Y = np.meshgrid(x_range, y_range)
    Z = 6 * X ** 2 + Y ** 2 - X * Y + X

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, color='lightgray', alpha=0.8)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Метод Флетчера-Ривса')

    for i in range(1, k + 1):
        ax.plot([x[i - 1].x, x[i].x], [x[i - 1].y, x[i].y], [f(x[k-1].x, x[k-1].y), f(x[k].x, x[k].y)], marker='o', color='red', linewidth=2, linestyle='-')

    plt.show()


x = {0: Point(2, 1.5)}
ep1 = 0.1
ep2 = 0.15
M = 10
k = 0

d = {}
final_p = x[0]
final_k = k
flag = False

while True:
    print(f'k = {k}, point = {x[k]}, grad = {x[k].gradient()}, norm = {x[k].gradient().norm()}')
    if x[k].gradient().norm() < ep1:
        final_p = x[k]
        final_k = k
        break
    if k >= M:
        final_p = x[k]
        final_k = k
        break
    elif k == 0:
        d[k] = -1 * x[k].gradient().np_point()
    else:
        b = ((x[k].gradient().norm())**2) / ((x[k-1].gradient().norm())**2)
        d[k] = -1 * x[k].gradient().np_point() + b*d[k-1]

    t = x[k].tk(d[k])
    print(f', d = {d[k]}, tk = {t}', end="")
    x[k+1] = x[k].point_add(t*d[k])
    print(f', norm2 = {x[k + 1].norm2(x[k])}\n')
    if x[k + 1].norm2(x[k]) > ep2 or abs(x[k + 1].f() - x[k].f()) > ep2 :
        k = k + 1
    else:
        if flag:
            final_k = k
            final_p = x[k]
            break
        else:
            flag = True
            k = k + 1



print('\nx* =', final_p)
print('f(x*) =', f(final_p.x, final_p.y))
print('k =', final_k)
visual_2d()
visual_3d()
