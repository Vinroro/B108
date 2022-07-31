# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

all_classes = []

class Class_of_students:
    def __init__(self, number, letter):
        self.number = number
        self.letter = letter.upper()
        self.students_list = []
        self.teachers_list = {}

        try:
            if 0 < self.number < 12 and self.letter in "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ":
                all_classes.append(str(self.number) + self.letter)
                print(f"Создан класс {self.number}{self.letter}")
            else:
                print("Некорректные вводные для создания учебного класса")
        except TypeError:
            print("Некорректные вводные для создания учебного класса")

    def add_student(self, student):
        self.students_list.append(student.fio)
        print(f"Ученик {student.fio} добавлен в учебный класс {self.number}{self.letter}")

    def add_teacher(self, teacher):
        if teacher.subject not in self.teachers_list:
            self.teachers_list[teacher.subject] = teacher.fio
            print(f"Теперь в классе {self.number}{self.letter} предмет {teacher.subject} преподаёт {teacher.fio}")
        else:
            self.teachers_list[teacher.subject] = teacher.fio
            print(f"Произошла замена. Теперь в классе {self.number}{self.letter} предмет {teacher.subject} преподаёт {teacher.fio}")

class Person:
    def __init__(self, surname, name, patronymic):
        self.surname = surname.upper()[0] + surname[1:]
        self.name = name.upper()[0] + name[1:]
        self.patronymic = patronymic.upper()[0] + patronymic[1:]
        self.fio = self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."

class Student(Person):
    def __init__(self, surname, name, patronymic, class_of_students, mother, father):
        super().__init__(surname, name, patronymic)
        self.class_of_students = class_of_students
        self.parents = (mother.fio, father.fio)

    def get_subjects(self):
        return [subject for subject in self.class_of_students.teachers_list.keys()]

class Parent(Person):
    def __init__(self, surname, name, patronymic):
        super().__init__(surname, name, patronymic)

class Teacher(Person):
    def __init__(self, surname, name, patronymic, subject):
        super().__init__(surname, name, patronymic)
        self.subject = subject

new_class = Class_of_students(1, "А")
new_class1 = Class_of_students(4, "Б")
new_class2 = Class_of_students(12, "А")
new_class3 = Class_of_students(1, "Ы")

parent = Parent("Виноградова", "Юлия", "Ивановна")
parent1 = Parent("Виноградов", "Геннадий", "Юрьевич")

student = Student("Виноградов", "Роман", "Геннадьевич", new_class, parent, parent1)
student1 = Student("Виноградов", "Владимир", "Геннадьевич", new_class, parent, parent1)
student2 = Student("Виноградова", "София", "Геннадьевна", new_class, parent, parent1)

teacher = Teacher("Иванов", "Пётр", "Сидорович", "Math")
teacher1 = Teacher("Сидоров", "Иван", "Петрович", "History")
teacher2 = Teacher("Петров", "Сидор", "Иванович", "History")

new_class.add_student(student)
new_class.add_student(student2)
new_class1.add_student(student1)

new_class.add_teacher(teacher)
new_class.add_teacher(teacher1)
new_class.add_teacher(teacher2)
new_class1.add_teacher(teacher)
new_class1.add_teacher(teacher1)

print()
# 1. Получить полный список всех классов школы
print(f"Полный список всех классов школы: {all_classes}")
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
print(f"Список всех учеников в классе {new_class1.number}{new_class1.letter}: {new_class1.students_list}")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
print(f"Список всех предметов ученика {student.fio}: {student.get_subjects()}")
# 4. Узнать ФИО родителей указанного ученика
print(f"ФИО родителей ученика {student.fio}: {student.parents}")
# 5. Получить список всех Учителей, преподающих в указанном классе
print(f"Список всех учителей класса {new_class1.number}{new_class1.letter}: {new_class1.teachers_list}")