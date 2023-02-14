# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
# not (X or Y or Z) = not X and not Y and not Z

userX = int(input('Введите значение для X: ')) # Строка ввода числа с текстом для пользователя
userY = int(input('Введите значение для Y: ')) # Строка ввода числа с текстом для пользователя
userZ = int(input('Введите значение для Z: ')) # Строка ввода числа с текстом для пользователя

if (not (userX or userY or userZ) == (not userX and not userY and not userZ)):
    print('Истинно так, дитя моё')
else:
    print('Машина говорит НАЙН')