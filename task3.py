# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from function import get_random_list
from function import get_difference_of_elements

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

list = get_random_list(
    int(numofelements), float(minelements), float(maxelements), "float"
)
print(f"Полученный список чисел: {list}")
print(
    f"Разница между максимальным и минимальным значением дробной части элементов: {get_difference_of_elements(list)}"
)
