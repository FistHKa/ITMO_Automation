# определяем функцию
def add(x, y):
    return x + y


# вызываем функцию
print(add(1, 2))

print(add('i a', 'm tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d

print(arg(1, 1, 1, 1))

print(arg(2, 2))

# print(arg(2, 2, '1', 1))


def task(a=(1, 2, 3, 4)):
    return a[1]


def circle(r, pi=3.14159):
    return pi * r ** 2

print(circle(2))