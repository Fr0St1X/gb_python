# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

dictionary = {}

usernumber = int(input('Введите число: '))
for i in range(1, usernumber + 1):
    dictionary [i] = 3*i + 1
print(dictionary)