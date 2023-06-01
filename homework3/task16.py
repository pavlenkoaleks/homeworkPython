#Задача 16: 
amount_of_elements = int(input('Введите количество элементов N: '))
from random import randint
my_list = []
counter=0

for i in range(amount_of_elements):
     my_list.append(randint(0,5))
print(my_list)
desired_number = int(input('Введите число, количество которых необходимо посчитать: '))

for i in range(amount_of_elements):
     if my_list[i]==desired_number:
         counter+=1
print(f"Количество чисел '{desired_number}': {counter}")