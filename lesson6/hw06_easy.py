import os
import sys

# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError:
    print("Значение переменной(ых) невозможно преобразовать к типу float")

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def exercise_2_dir_creation():

    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), f"dir_{i}")
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print("Такая директория уже существует")

    print("Скрипт exercise_2_dir_creation выполнен")

def exercise_2_dir_deletion():

    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), f"dir_{i}")
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print("Такой директории не существует")

    print("Скрипт exercise_2_dir_deletion выполнен")

exercise_2_dir_creation()
exercise_2_dir_deletion()

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

def exercise_2_dir_list():

    dir_list = os.listdir(os.getcwd())

    for i in dir_list:
        if os.path.isdir(i):
            print(i)

    print("Скрипт exercise_2_dir_list выполнен")

exercise_2_dir_list()

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def exercise_2_copy_creation():
    fw = open(os.path.join("file_copy.py"), "w", encoding="UTF-8")
    fr = open(os.path.join(sys.argv[0]), "r", encoding="UTF-8")

    lines = fr.readlines()

    for line in lines:
        fw.write(line)

    fw.close()
    fr.close()

    print("Скрипт exercise_2_copy_creation выполнен")

exercise_2_copy_creation()