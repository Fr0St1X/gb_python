# Сложить числа вещественного числа

usernumber = str(input('Введите число: ')) # Строка ввода числа с числом для пользователя
userstring = usernumber.replace('.', '').replace(',', '').replace('-', '').replace('+', '').replace(' ', '') # Замена возможных символов
if userstring.isdigit(): # Проверка на корретность введённых данных
    userlist = list(userstring) # Преобразует символы в список
    usersum = 0 # Задаём переменную суммы равной нулю
    for listnumber in userlist: # Цикл для сложения всех цифр в списке userlist
        usersum = usersum + int(listnumber) # Сложение с преобразованием списка в числа
    print(f'Сумма вещественного числа равна {usersum}') # Вывод

else:
    print('Некорретные данные') # Сообщение об ошибке