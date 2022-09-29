# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from function import get_random_list
from function import get_composition_paired_list_items

numofelements, minelements, maxelements = (
    input("Введите четное количесво элементов списка: "),
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

if int(numofelements) % 2 != 0:
    print("Вы ввели не четное количество элементов")
    quit()


list = get_random_list(int(numofelements), int(minelements), int(maxelements))
print(f"Полученный список чисел: {list}")
print(
    f"Произведение пар чисел списка: {get_composition_paired_list_items(list)}")
