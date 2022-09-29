from random import randint
from random import uniform


def getrandomlist(lenlist=10, minlist=0, maxlist=10, type="int"):
    randlist = []
    if type == "int":
        for i in range(1, lenlist + 1):
            randlist.append(randint(minlist, maxlist + 1))
    if type == "float":
        for i in range(1, lenlist + 1):
            randlist.append(round(uniform(minlist, maxlist + 1),2))
    return randlist


def getsummoddposition(list):
    summ = 0
    for i in range(1, len(list), 2):
        summ += int(list[i])
    return summ


def getcompositionpairedlistitems(list):
    resultlist = []
    for i in range(len(list) // 2):
        resultlist.append(list[i] * list[len(list) - i - 1])
    return resultlist


def getdifferenceofelements(list):
    remainslist=[]
    for i in range(len(list)):
        remainslist.append()