# Показать первую цифру дробной части числа

usernumber = float(input('Введите число: ')) # Строка ввода первого числа с текстом для пользователя

roundednumber = round(usernumber, 1) # Округляем число до одного символа после запятой
roundedstring = str(roundednumber) # Преобразуем float в string
print(roundedstring) # Вывод последнего числа