# Функция нахождения значения функции
def getFuncValue(x):
    if x == 1 or x == -1:
        return 'Ошибка: ' + str(int(x)) + ' - недопустимое значение X'

    return 'Y = ' + str((x ** 2 + 1) / (3 * (x ** 2 - 1)) + (x ** 2 - 1) * (1 - x))

# Получаем значение x
x = float(input('Введите значение X >> '))

# Выводим ответ
print(getFuncValue(x))