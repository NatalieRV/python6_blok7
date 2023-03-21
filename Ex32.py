# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
list = input('Введите числа через пробел: ').split()
print(list)
a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
result = []
for i in range(len(list)):
    if int(list[i])>a and int(list[i])<b:
        result.append(i)
print(result)