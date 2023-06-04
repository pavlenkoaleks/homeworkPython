#Задача 26: 
numb1 = int(input('Введите число для возведения в степень: '))
degree1 = int(input('Введите степень числа: '))

def exponentiation(numb,degree):
     if degree == 0:
        return 1
     return numb * exponentiation(numb, degree - 1)

print(exponentiation(numb1,degree1))


