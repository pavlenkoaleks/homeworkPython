elements = int(input("Введите количество элементов списка "))

from random import randint
list_1 = []
for i in range(elements):
     list_1.append(randint(0,10))
print(list_1)
min_number = int(input("Введите минимальное значение "))
max_number = int(input("Введите максимальное значение "))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
       print(i)