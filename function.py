from random import randint
from random import uniform


def get_random_list(len_list=10, min_list=0, max_list=10, type="int"):
    rand_list = []
    if type == "int":
        for i in range(1, len_list + 1):
            rand_list.append(randint(min_list, max_list + 1))
    if type == "float":
        for i in range(1, len_list + 1):
            rand_list.append(round(uniform(min_list, max_list + 1), 2))
    return rand_list


def get_sum_modd_position(list):
    summ = 0
    for i in range(1, len(list), 2):
        summ += int(list[i])
    return summ


def get_composition_paired_list_items(list):
    result_list = []
    for i in range(len(list) // 2):
        result_list.append(list[i] * list[len(list) - i - 1])
    return result_list


def get_difference_of_elements(list):
    remains_list = []
    for i in range(len(list)):
        remains_list.append(list[i] - int(list[i]))
    max = remains_list[0]
    min = remains_list[0]
    for i in range(1, len(remains_list)):
        if remains_list[i] > max:
            max = remains_list[i]
        if remains_list[i] < min:
            min = remains_list[i]
    return round(max - min, 2)


def get_binary_number(number):
    binary_number = ""
    while number != 0:
        binary_number = str(number % 2)+binary_number
        number //= 2
    return binary_number


def get_fibonacci(number):
    fibonacci_nums_list = []
    first, second = 1, 1
    for i in range(number):
        fibonacci_nums_list.append(first)
        first, second = second, first + second
    first, second = 0, 1
    for i in range(number+1):
        fibonacci_nums_list.insert(0, first)
        first, second = second, first - second
    return fibonacci_nums_list
