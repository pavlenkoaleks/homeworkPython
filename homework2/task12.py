#Задача 12: 
summ = int(input('Введите сумму чисел '))
proizvedenie = int(input('Введите произведение чисел '))

from math import sqrt
Y1=(summ+sqrt(summ*summ -4*proizvedenie))/2
X1 = summ-Y1

if (Y1<0 or X1<0):
    Y2=(summ-sqrt(summ*summ -4*proizvedenie))/2
    X2 = summ-Y2
    print(f"числа, задуманные Петей: {int(X2),int(Y2)}")
else:
    print(f"числа, задуманные Петей: {int(X1),int(Y1)}")
      
