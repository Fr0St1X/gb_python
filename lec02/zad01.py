# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

list = []
n = 1
usernumber = int(input('Введите число: '))

for i in range(usernumber):
    list.append(n)
    n *= -3
print(list)