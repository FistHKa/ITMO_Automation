def task_1(a, b):
    if a > b:
        print(a)
    else:
        print(b)
task_1(1, 5)


def task_2(a, b):
    if abs(a - b) == 135:
        print('YES')
    else:
        print('NO')
task_2(100, 235)


def task_3(a):
    if a in range(1, 3) or a == 12:
        print('Зима')
    elif a in range(3, 6):
        print('Весна')
    elif a in range(6, 9):
        print('Лето')
    elif a in range(9, 12):
        print('Осень')
    else:
        print('Введите корректный месяц')
task_3(12)


def task_4(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')
task_4(24, 8, 37)


task_5_list = [-12, 4, 0, -19, 102]
count = 0
for elem in task_5_list:
    if elem > 0:
        count = count + 1
    else:
        count = count
print('Количество положительных чисел = ', count)


def task_6(number_of_years: int, number_of_months: int):
    return ((number_of_years * 12) + number_of_months) * 29
print('Количество дней = ', task_6(2, 4))


