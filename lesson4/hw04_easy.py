# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили

def convert(km):
    miles = 1609 * int(km)
    print(miles)

convert(10)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    return f"{float(str(number)):.{ndigits}f}"


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    str_ticket_number = str(ticket_number)

    if len(str_ticket_number) == 6:
        sum1 = int(str_ticket_number[0]) + int(str_ticket_number[1]) + int(str_ticket_number[2])
        sum2 = int(str_ticket_number[3]) + int(str_ticket_number[4]) + int(str_ticket_number[5])
    else:
        return False

    if sum1 == sum2:
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
