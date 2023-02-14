# Вывести на экран числа от -N до N

usernumber = int(input('Введите число: ')) # Строка ввода числа с текстом для пользователя

for i in range(-usernumber, usernumber+1):
    print(i)