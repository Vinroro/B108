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


# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
# except ValueError:
#     print("a и b должны быть типа float")
# else:
#     c = avg(a, b)
#     print("Среднее геометрическое = {:.2f}".format(c))

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def exercise_2_dir_creation(dir_path):
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print("Такая директория уже существует")
    else:
        print(f"Директория {dir_path} создана")


def exercise_2_dir_creation_x10():
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), f"dir_{i}")
        exercise_2_dir_creation(dir_path)


def exercise_2_dir_deletion(dir_path):
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print("Такой директории не существует")
    else:
        print(f"Директория {dir_path} удалена")


def exercise_2_dir_deletion_x10():
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), f"dir_{i}")
        exercise_2_dir_deletion(dir_path)


# exercise_2_dir_creation_x10()
# exercise_2_dir_deletion_x10()

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.


def exercise_2_dir_list():
    dir_list = os.listdir(os.getcwd())
    print("Папки текущей директории:")
    for i in dir_list:
        if os.path.isdir(i):
            print(i)


# exercise_2_dir_list()


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def exercise_2_copy_creation():
    f_to_write = open(os.path.join("file_copy.py"), "w", encoding="UTF-8")
    f_to_read = open(os.path.join(sys.argv[0]), "r", encoding="UTF-8")
    with f_to_write, f_to_read:
        lines = f_to_read.readlines()
        for line in lines:
            f_to_write.write(line)
        print(f"Копия файла {sys.argv[0]} создана")


# exercise_2_copy_creation()
