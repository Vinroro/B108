# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def arith_ops_with_fractions(expression):
    components = expression

    # Определяем: сложение или вычитание. Записываем компоненты выражения
    if " + " in components:
        components = expression.split(" + ")
        operation = "+"
    else:
        components = expression.split(" - ")
        operation = "-"

    # Записываем целую часть в int_parts, дробную - во fract_parts
    for i in components:
        components[components.index(i)] = i.split(" ")

    int_parts = []
    fract_parts = []
    for i in components:
        if len(i) == 2:
            int_parts.append(i[0])
            fract_parts.append(i[1])
        else:
            if "/" not in i[0]:
                int_parts.append(i[0])
                fract_parts.append("0/1")
            else:
                int_parts.append("0")
                fract_parts.append(i[0])

    # Если целая часть отрицательная, то делаем дробную отрицательной
    for i in int_parts:
        if "-" in i:
            fract_parts[int_parts.index(i)] = "-" + fract_parts[int_parts.index(i)]

    # Определяем общий знаменатель, числитель1 и числитель2
    denominator = int(fract_parts[0].split("/")[1]) * int(fract_parts[1].split("/")[1])
    numerator1 = (int(int_parts[0]) * denominator) + (
                int(fract_parts[0].split("/")[0]) * int(fract_parts[1].split("/")[1]))
    numerator2 = (int(int_parts[1]) * denominator) + (
                int(fract_parts[1].split("/")[0]) * int(fract_parts[0].split("/")[1]))

    # Исходя из вида операции (сложение или вычитание), производим вычисление и готовим вывод заданного формата
    if operation == "+":
        numerator = numerator1 + numerator2
    else:
        numerator = numerator1 - numerator2

    n = numerator // denominator
    x = numerator % denominator
    y = denominator

    if x == 0:
        result = str(n)
    else:
        result = str(n) + " " + str(x) + "/" + str(y)

    return result

print(arith_ops_with_fractions("-2/3 - -2"))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
