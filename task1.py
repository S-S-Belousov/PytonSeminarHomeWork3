# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from function import getrandomlist
from function import getsummoddposition

numofelements, minelements, maxelements = (
    input("Введите количесво элементов списка: "),
    input("Введите минимальное значение элемента списка: "),
    input("Введите максимальное значение элемента списка: "),
)

if (
    numofelements.isdigit() == False
    or int(numofelements) < 1
    or minelements.isdigit() == False
    or maxelements.isdigit() == False
):
    print("Вы ввели недопустимое значение")
    quit()

list = getrandomlist(int(numofelements), int(minelements), int(maxelements))
print(f"Полученный список чисел: {list}")
print(f"Сумма четных элементов: {getsummoddposition(list)}")
