# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным

usernumber = int(input('Введите номер дня недели: ')) # Строка ввода числа с текстом для пользователя

# Проверка условий и вывод данных
if usernumber == 1:
    print(f'День №{usernumber} это понедельник. Опять работа...')
    quit()
if usernumber == 2:
    print(f'День №{usernumber} это вторник. Опять работа...')
    quit()
if usernumber == 3:
    print(f'День №{usernumber} это среда. Опять работа...')
    quit()
if usernumber == 4:
    print(f'День №{usernumber} это четверг. Опять работа...')
    quit()
if usernumber == 5:
    print(f'День №{usernumber} это пятница. Опять работа...')
    quit()
if usernumber == 6:
    print(f'День №{usernumber} это суббота. Кто идёт за Клинским?')
    quit()
if usernumber == 7:
    print(f'День №{usernumber} это воскресенье. Кто идёт за Клинским?')
    quit()
else:
    print(f"{usernumber} это не номер дня недели!")