lambda_k = lambda x, y, l, r: l + r * (x + y - 1)

x1 = lambda l, r: (-8 - 10 * l + 9 * r) / (44 + 18 * r)
x2 = lambda l, r: (-2 - 8 * l + 9 * r) / (44 + 18 * r)

p = lambda x, y, l, r: l * (x + y - 1) + (r / 2) * ((x + y - 1) ** 2)

f = lambda x, y: 3 * x ** 2 + 4 * y ** 2 - x * y + x

pk = 10000
e = 0.001

lk = [0]
rk = [1, 2, 10, 100, 1000]

k = 0
while (pk > e):
    x_1 = x1(lk[k], rk[k])
    x_2 = x2(lk[k], rk[k])
    pk = p(x_1, x_2, lk[k], rk[k])
    print(f'k={k}, l={lk[k]}, x1={x_1}, x2={x_2}, P={format(pk, '.8f')}, f={f(x_1, x_2)}')
    lk.append(lambda_k(x_1, x_2, lk[k], rk[k]))
    k += 1
