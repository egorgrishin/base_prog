import lab6.helper as Helper
import numpy


def main(input_name, output_name):
    input_file = Helper.getFile(input_name)
    if not input_file:
        print('Файл с входными данными не обнаружен')
        return False

    number = input_file.readline()
    if not Helper.isNumber(number):
        print('В файле указаны некорректные данные')
        return False

    number_data = getNumberData(number)
    result = getCountedNumber(number_data)

    output_file = Helper.getFile(output_name, 'w')
    Helper.outputResult(result, output_file)


def getNumberData(number):
    number_list = list(map(int, number))

    return {
        'number': number,
        'amount': len(number),
        'sum': numpy.sum(number_list),
        'prod': numpy.prod(number_list),
    }


def getCountedNumber(counted_data):
    return f"""Число: {counted_data['number']}
Количество цифр: {counted_data['amount']}
Сумма цифр: {counted_data['sum']}
Произведение цифр: {counted_data['prod']}"""


main('input.txt', 'output.txt')
