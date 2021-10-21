def getRow(data):
    col_width = 30
    return data + ' ' * (col_width - len(data))

table = []
amount_conscripts = int(input('Информацию о скольки призывниках вы хотите заполнить? '))
if amount_conscripts < 0:
    print('Некорректное число')
elif amount_conscripts == 0:
    print('Завершаем')
else:
    print('Ввод информации в формате Фамилия Имя Отчество Год рождения Заболевание (через пробел)')
    for i in range(amount_conscripts):
        is_correct = False
        while not is_correct:
            info = input(f'Введите информацию о призывнике {i + 1}: ')
            ar_info = info.split(' ')
            if len(ar_info) == 5:
                is_correct = True
                table.append(info.split(' '))

    row = '№    '
    row += getRow('Фамилия')
    row += getRow('Имя')
    row += getRow('Отчество')
    row += getRow('Год рождения')
    row += getRow('Заболевание')
    print(row + '\n' + '-' * len(row))

    i = 0
    for conscript in table:
        i += 1
        str_i = str(i)
        row = str_i + ' ' * (5 - len(str_i))
        for data in conscript:
            row += getRow(data)
        print(row)
