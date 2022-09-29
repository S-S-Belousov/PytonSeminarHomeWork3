# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
from function import get_fibonacci

number = int(input("Введите целое число: "))

print(f'Cписок чисел Фибоначчи: {get_fibonacci(number)}')
