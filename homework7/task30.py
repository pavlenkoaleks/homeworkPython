first_element = int(input("Введите первое элемент прогрессии "))
diff = int(input("Введите разность элементов прогресии "))
quantity = int(input("Введите количество элементов прогресии "))

my_list =[]

for i in range(quantity):
    my_list.append(first_element+i*diff)



print(my_list)