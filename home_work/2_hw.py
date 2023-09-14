def task_1() -> str:
    a: int = 1
    b: float = 1.2
    c: str = 'line'
    d: list = [1, 3, 5]
    e: bool = 10 > 5
    print(a, 'относится к типу', type(a))
    print(b, 'относится к типу', type(b))
    print(c, 'относится к типу', type(c))
    print(d, 'относится к типу', type(d))
    print(e, 'относится к типу', type(e))
task_1()


def task_2() -> list:
    a: list = [1, 2, 3, 5, 8, 13, 21] # Последовательность Фибоначчи
    return a[0:3]
print(task_2())

def task_3(a: int) -> int:
    return a ** 2
print(task_3(5))