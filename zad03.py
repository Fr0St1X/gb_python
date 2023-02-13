# Вывести на экран числа от -N до N

usernumber = int(input('Введите число: ')) # Строка ввода первого числа с текстом для пользователя

for i in range(-usernumber, usernumber+1):
    print(i)