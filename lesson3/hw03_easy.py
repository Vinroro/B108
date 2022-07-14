# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]

max_len = 0

for i in fruits:
    if len(i) > max_len:
        max_len = len(i)

for fruit in fruits:
    print("{}. {:>{}}".format(fruits.index(fruit) + 1, fruit, max_len))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

fruits = ["яблоко", "банан", "киви", "арбуз"]
importFruits = ["банан", "киви"]

for importFruit in importFruits:
    for fruit in fruits:
        if importFruit == fruit:
            fruits.pop(fruits.index(fruit))

print(fruits)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbaz = [1, 6, 0, 3, 4]
newNumbaz = []

for number in numbaz:
    if number % 2 == 0:
        number /= 4
    else:
        number *= 2
    newNumbaz.append(number)

print(newNumbaz)