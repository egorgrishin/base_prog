import os
import numpy as np


def main(file):
    file_list = os.listdir()

    if not checkFile(file, file_list):
        print('Файл с входными данными не обнаружен')
        return False

    f = open(file)
    number = f.readline()

    if not isNumber(number):
        print('В файле указаны некорректные данные')
        return False

    printCountedNumber(getNumberCount(number))


def checkFile(file, file_list):
    return file in file_list
    # Можно было return os.path.exists('input.txt')


def isNumber(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def getNumberCount(number):
    number_list = list(map(int, number))

    return {
        'number': number,
        'amount': len(number),
        'sum': np.sum(number_list),
        'prod': np.prod(number_list),
    }


def printCountedNumber(counted_data):
    f = open('output.txt', 'w')
    f.write(f"""Число: {counted_data['number']}
Количество цифр: {counted_data['amount']}
Сумма цифр: {counted_data['sum']}
Произведение цифр: {counted_data['prod']}""")
    f.close()


main('input.txt')
