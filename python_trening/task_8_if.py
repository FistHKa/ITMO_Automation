# Программа проверяет является число положительным
# или отрицательным и выводит соответствующее сообщение.

# num = 3

# num = 5
# num = 0

# if num >= 0:
#     print('Число больше либо равно нулю')
# else:
#     print('Число отрицательное')

# def task_yes_no(str_1, str_2):
#     if str_1 in str_2:
#         print("Да")
#     else:
#         print("Нет")
#
# task_yes_no(str_1='test', str_2='test1')


# num_float = 3.4
# num_float = 0
# num_float = -3.2
#
# if num_float > 0:
#     print('Положительное число')
# elif num_float == 0:
#     print('Ноль')
# else:
#     print('Число отрицательное')


# permit_print = True
#
# if num > 0 and permit_print:
#     print('num - положительное число')
# elif not permit_print:
#     print('Печать запрещена')

# def name_course(a):
#     if a >= 1 and a <= 4:
#         print('Бакалавр')
#     elif a in range(5, 7):
#         print('Магистр')
#     elif a in range(7, 10):
#         print('Аспирант')
#     else:
#         print('Введите корректный год обучения')
# name_course(12)

def number(a):
    if a > 100 or a < -100:
        print('-')
    else:
        print('+')
number(0)