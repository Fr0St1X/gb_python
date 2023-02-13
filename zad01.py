# По двум заданным числам проверить является ли одного квадратом второго

if firstusernumber == secondusernumber: # Условие №1
    print('Зачем одинаковые числа даёшь? Обидеть хочешь?')
    quit()
if firstusernumber % secondusernumber == 0: # Условие №2
    print('Первое число является корнем второго.')
    quit()
if secondusernumber % firstusernumber == 0: # Условие №3
    print('Второе число является корнем первого.')
    quit()
else: # Ни одно условие не подходит
    print('Ни одно число не является корнем другого.')
    quit()