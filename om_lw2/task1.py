import math
import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    # f = lambda self: 6 * (self.x ** 2) + self.y ** 2 - self.x * self.y + self.x
    # f_divX = lambda self: 12 * self.x - self.y + 1
    # f_divY = lambda self: 2 * self.y - self.x

    f = lambda self: 3 * (self.x ** 2) + 4 * (self.y ** 2) - 2 * self.x * self.y + self.x
    f_divX = lambda self: 6 * self.x - 2 * self.y + 1
    f_divY = lambda self: 8 * self.y - 2 * self.x

    def gradient(self):
        return Point(self.f_divX(), self.f_divY())

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    def norm2(self, p):
        return math.sqrt((p.x-self.x)**2 + (p.y-self.y)**2)

    def tk(self):
        return (self.f_divX()**2 + self.f_divY()**2) / (6 * (self.f_divX()**2) - 4  * self.f_divX() * self.f_divY() + 8 * (self.f_divY() ** 2))

    def new_point(self):
        p = self.gradient()
        t = self.tk()
        return Point(self.x - t * p.x, self.y - t*p.y)

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
    plt.title('Градиентный спуск')
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
    plt.title('Градиентный спуск')

    for i in range(1, k + 1):
        ax.plot([x[i - 1].x, x[i].x], [x[i - 1].y, x[i].y], [x[i - 1].f(), x[i].f()], marker='o', color='red', linewidth=2, linestyle='-')

    plt.show()


x = {0: Point(2, 1.5)}
ep1 = 0.1
ep2 = 0.15
M = 10
k = 0
n = 0
final_x = x[0]
final_k = k
flag = False

while True:
    print(f'k = {k}, point = {x[k]}, grad = {x[k].gradient()}, norm = {x[k].gradient().norm()}, tk = {x[k].tk()}, \nnew_point = {x[k].new_point()}, norm2 = {x[k].new_point().norm2(x[k])}')
    if x[k].gradient().norm() < ep1:
        final_x = x[k]
        final_k = k
        break
    if k >= M:
        final_x = x[k]
        final_k = k
        break
    x[k + 1] = x[k].new_point()
    if x[k + 1].norm2(x[k]) > ep2 or abs(x[k + 1].f() - x[k].f()) > ep2:
        k = k + 1
    else:
        if flag:
            final_k = k
            final_x = x[k]
            break
        else:
            flag = True
            k = k + 1
    print()
print('x* =', x[k])
print('f(x*) =', x[k].f())
print('k =', k)
visual_2d()
visual_3d()