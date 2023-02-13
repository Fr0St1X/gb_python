# По двум заданным числам проверить является ли одного квадратом второго

firstusernumber = float(input('Введите первое число: ')) # Строка ввода первого числа с текстом для пользователя
secondusernumber = float(input('Введите второе число: ')) # Строка ввода второго числа с текстом для пользователя

if firstusernumber == secondusernumber:
    print('Зачем одинаковые числа даёшь? Обидеть хочешь?')
    quit()
if firstusernumber % secondusernumber == 0: # Условие №1
    print('Первое число является корнем второго.')
    quit()
if secondusernumber % firstusernumber == 0: # Условие №2
    print('Второе число является корнем первого.')
    quit()
else:
    print('Ни одно число не является корнем другого.')
    quit()