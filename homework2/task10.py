#Задача 10: 
n_coins = int(input('Введите количество монеток '))
count =0
from random import randint
for i in range(n_coins):
     SideofCoin=randint(0,1)
     print(SideofCoin)
     if (SideofCoin==1):
           count += 1
     
if count>=n_coins/2 :
      print(f"переверни {n_coins-count } монет")
else:
      print(f"переверни {count} монет")