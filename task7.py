""" Напишите программу, которая принимает на вход
    вещественное число и показывает сумму его цифр.
    Пример:
    - 6782 -> 23
    - 0,56 -> 11                                """

n = input('Введите вещественное число: ')
sum_of_digit = 0
for elem in n:
    if elem.isdigit():
        sum_of_digit += int(elem)
print(f'  {n} -> {sum_of_digit}')