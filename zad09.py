# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

usertext = int(input('Введите требуемую четверть системы координат: ')) # Строка ввода числа с текстом для пользователя

# if userX > 0 and userY > 0:
#     print('I четверть')
# if userX < 0 and userY > 0:
#     print('II четверть')
# if userX < 0 and userY < 0:
#     print('III четверть')
# if userX > 0 and userY < 0:
#     print('IV четверть')
# if userX == 0 and userY == 0:
#     print('в начале координат')

if usertext == 1:
    print('X и Y должены быть больше нуля.')
    quit()
if usertext == 2:
    print('X должен быть меньше нуля, Y должен быть больше нуля.')
    quit()
if usertext == 3:
    print('X и Y должны быть меньше нуля.')
    quit()
if usertext == 4:
    print('X должен быть больше нуля, Y должен быть меньше нуля.')
    quit()
else:
    print('Введены неверные данные')