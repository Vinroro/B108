# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibonacci_list = [1, 1]

    for i in range(m):
        fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i + 1])

    return fibonacci_list[n:]

print(fibonacci(0, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    result_list = []
    origin_list_copy = origin_list.copy()

    while len(result_list) != len(origin_list):
        result_list.append(min(origin_list_copy))
        origin_list_copy.remove(min(origin_list_copy))

    return result_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def check_for_filter(i):
    return i > 0

def my_filter_realisation(filter, list):
    result_list = []

    for i in list:
        if filter(i):
            result_list.append(i)

    return result_list

print(my_filter_realisation(check_for_filter, [-1, 0, 1]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def p_m_check(a1, a2, a3, a4):
    return round(a1[0] + a3[0]) == round(a2[0] + a4[0]) and round(a1[1] + a3[1]) == round(a2[1] + a4[1])

print(p_m_check([-4, -1], [-2, 3], [4, 5], [2, 1]))