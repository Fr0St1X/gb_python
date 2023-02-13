# Показать первую цифру дробной части числа

usernumber = float(input('Введите число: ')) # Строка ввода первого числа с текстом для пользователя

roundednumber = round(usernumber, 1)
roundedstring = str(roundednumber)
print(roundedstring[-1])