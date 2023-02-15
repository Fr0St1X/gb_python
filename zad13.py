# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой
# ufs = User's First String
# uss = User's First String

ufs = str(input('Введите первую строку: ')) # Первая строка ввода пользователя
uss = str(input('Введите вторую строку: ')) # Вторая строка ввода пользователя

samechars = 0 # Переменная одинаковых символов

for chars in ufs: # Для символов в певой строке
    if chars in uss: # Сравнить с символами во второй строке
        samechars += 1 # Счетчик одинаковых символов, и передача их количества (через + 1) в переменную samechars

print(f'Количество вхождений {samechars}') #Вывод