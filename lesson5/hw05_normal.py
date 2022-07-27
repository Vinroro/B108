# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

string = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# re solution
pattern = "[A-Z]*([a-z]+)[A-Z]*"
found = re.findall(pattern, string)

print(found)

# no re solution
# Очищаем строку от символов, не являющихся латиницей
for i in string:
    if i not in list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
        string = string.replace(i, "")

# Заменяем символы верхнего регистра на пробел
for i in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    string = string.replace(i, " ")

# Делим строку по пробелам и очищаем список от пустых элементов для получения искомого результата
found2 = string.split(" ")

while "" in found2:
    found2.remove("")

print(found2)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

import re

string = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

#re solution
pattern = "[a-z]{2}([A-Z]+)[A-Z]{2}"
found = re.findall(pattern, string)

print(found)

#no re solution
# Очищаем строку от символов, не являющихся латиницей
for i in string:
    if i not in list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
        string = string.replace(i, "")

# Заменяем символы нижнего регистра на пробел
for i in list("abcdefghijklmnopqrstuvwxyz"):
    string = string.replace(i, " ")

# Получаем список элементов, находящихся справа от 2 символов нижнего регистра
found2 = string.split("  ")

# Подходящие условию элементы не могут быть короче 3-х символов, так как в их конце должно быть ещё минимум 2 символа
# в верхнем регистре
found3 = []
for i in found2:
    if len(i) >= 3:
        found3.append(i)

# В начале элементов могли остаться пробелы (бывшие символы нижнего регистра), избавляемся от них
found4 = []
for i in found3:
    while i[0] == " ":
        i = i[1:]
    found4.append(i)

# Избавляемся от элементов, которые содержат в себе пробел с 0 по 2 символ включительно, которые должны состоять
# исключительно из символов верхнего регистра для соответствия условию
found5 = []
for i in found4:
    if " " not in i[:3]:
        found5.append(i)

# Оставляем части элементов до первого пробела и элементы без пробелов. Останутся элементы, состоящие только из
# элементов верхнего регистра
found6 = []
for i in found5:
    if " " in i:
        found6.append(i[:i.index(" ")])
    else:
        found6.append(i)

# Очищаем элементы от последних 2-х символов верхнего регистра для соответствия 2-му условию задачи
result = []
for i in found6:
    result.append(i[:-2])

# Очищаем список от пустых элементов. STONKS!
while "" in result:
    result.remove("")

print(result)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import os
import random

path = os.path.join("text.txt")

f = open(path, "w", encoding="UTF-8")

for i in range(2500):
    f.write(str(random.randint(0, 9)))

f.close()

f = open(path, "r", encoding="UTF-8")

string = f.read()
result = ""
operation = string[0]

for i in string[1 : len(string)]:
    if i == operation[0]:
        operation += i
    else:
        if len(operation) > len(result):
            result = operation
        operation = i

if len(operation) > len(result):
    result = operation

print(result)

f.close()