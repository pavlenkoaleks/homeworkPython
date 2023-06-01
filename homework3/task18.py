#Задача 18: 
amount_of_elements = int(input('Введите количество элементов N: '))
from random import randint
my_list = []
ABS_diff= float("inf") #модуль разности чисел

for i in range(amount_of_elements):
     my_list.append(randint(0,100))
print(my_list)
number = int(input('Введите число, к которому нужно найти максимально близкое: '))
Close_number=my_list[0]

for i in range(amount_of_elements):
     if ABS_diff>(abs(my_list[i]-number)):
         ABS_diff=abs(my_list[i]-number)
         Close_number=my_list[i]
print(f"самый близкий по величине элемент к заданному числу '{number}': {Close_number}")