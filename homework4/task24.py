#Задача 24: 
n_kust = int(input('Введите количество кустов: '))

from random import randint
berries = []

for i in range(n_kust):
     berries.append(randint(0,10))

print(berries)

max_berry = float("-inf") 
number_of_berries=0

for i in range(n_kust):
    if (i==n_kust-1):
        number_of_berries=berries[i]+berries[i-1]+berries[0]
    else:
        number_of_berries=berries[i]+berries[i-1]+berries[i+1]
    
    if number_of_berries>max_berry:
          max_berry=number_of_berries

print(f"максимальное количество ягод за один подход = {max_berry}")
          
