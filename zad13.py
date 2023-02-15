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
uss_list = uss.split()

samewords = 0 # Переменная одинаковых слов
for words in ufs_list: # Слова в первой строке
    if words in uss_list: # Сравнить со словами во второй строке
        samewords += 1 # Счетчик одинаковых слов, и передача их количества (через + 1) в переменную samewords

print(f'Количество вхождений {samewords}') #Вывод