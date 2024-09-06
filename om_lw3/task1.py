x1 = lambda r: (-8 + 9 * r) / (44 + 18 * r)
x2 = lambda r: (-2 + 9 * r) / (44 + 18 * r)

p = lambda x, y, r: (r / 2) * ((x + y - 1) ** 2)

f = lambda x, y: 3 * x ** 2 + 4 * y ** 2 - x * y + x

F = lambda x, y, r: f(x, y) + p(x, y, r)

pk = 10000
e = 0.001

rk = [1, 2, 10, 100, 1000, 10000]

k = 0
while (pk > e):
    x_1 = x1(rk[k])
    x_2 = x2(rk[k])
    pk = p(x_1, x_2, rk[k])
    print(f'k={k}, x1={x_1}, x2={x_2}, F={F(x_1, x_2, rk[k])} P={format(pk, '.8f')}, f={f(x_1, x_2)}')
    k += 1


print(f(0.5, 0.5))