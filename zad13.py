# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой
# ufs = User's First String
# uss = User's First String

# Строки ввода пользователя
ufs = str(input('Введите первую строку: ')) 
uss = str(input('Введите вторую строку: '))

# Удаление символов в строках
ufs = ufs.replace('.', '').replace(',', '').replace('-', '').replace('+', '').replace('!', '').replace('?', '') 
uss = uss.replace('.', '').replace(',', '').replace('-', '').replace('+', '').replace('!', '').replace('?', '') 

# Перевод строк в нижний регистр для упрощения выборки
ufs = ufs.lower() 
uss = uss.lower()

# Преобразование строк в списки
ufs_list = ufs.split()
print(ufs_list)
uss_list = uss.split()

samechars = 0 # Переменная одинаковых символов
for chars in ufs_list: # Для символов в первой строке
    if chars in uss_list: # Сравнить с символами во второй строке
        samechars += 1 # Счетчик одинаковых символов, и передача их количества (через + 1) в переменную samechars

print(f'Количество вхождений {samechars}') #Вывод