# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
from function import get_binary_number

number = input("Введите целое число: ")

if number.isdigit() == False:
    print("Вы ввели недопустимое значение")
    quit()

print(f"Число {number} в двочном коде: {get_binary_number(int(number))}")
