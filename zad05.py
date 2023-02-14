# Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

usernumber = int(input('Введите число: ')) # Строка ввода первого числа с текстом для пользователя

if usernumber % 5 == 0: # Проверка на кратность пяти
    print(f'{usernumber} кратно пяти.')
else:
    print(f'{usernumber} некратно пяти.')

if usernumber % 10 == 0: # Проверка на кратность десяти
    print(f'{usernumber} кратно десяти.')
else:
    print(f'{usernumber} некратно десяти.')

if usernumber % 15 == 0: # Проверка на кратность пятнадцати
    print(f'{usernumber} кратно пятнадцати.')
else:
    print(f'{usernumber} некратно пятнадцати.')

if usernumber % 30 == 0:# Проверка на кратность тридцати
    print(f'{usernumber} кратно тридцати.')
else:
    print(f'{usernumber} некратно тридцати.')