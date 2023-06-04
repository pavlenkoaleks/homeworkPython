#Задача 22: 
elements1 = int(input('Введите количество элементов N(первое множество): '))
elements2 = int(input('Введите количество элементов M(второе множество): '))
from random import randint
my_list1 = []
my_list2 = []
union_set={None}

for i in range(elements1):
     my_list1.append(randint(0,10))
for i in range(elements2):
     my_list2.append(randint(0,10))
print(my_list2)
print(my_list1)

union_set.update(my_list1)
union_set.remove(None)
union_set.update(my_list2)
print(*union_set)
