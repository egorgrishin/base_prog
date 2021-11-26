import lab6.helper as Helper
import module as Module
from datetime import datetime


def main(input_name, output_name):
    # Получаем дату начала выполнения программы
    first_datetime = datetime.now()

    # Проверяем наличие входного и открываем его
    input_file = Helper.getFile(input_name)
    if not input_file:
        print('Файл с входными данными не обнаружен')
        return False

    # Читаем входные данные и проверяем их корректность
    radius = input_file.readline()
    if not Helper.isNumber(radius):
        print('В файле указаны некорректные данные')
        return False

    # Читаем входные данные и проверяем их корректность
    coordinates = input_file.readline().split()
    if not Helper.isNumbersList(coordinates) or len(coordinates) != 2:
        print('В файле указаны некорректные данные')
        return False

    # Производим вычисления и оставляем временные метки
    points_count = Module.getPointsCount(coordinates, radius)
    result = Module.getResult(points_count, first_datetime)

    # Открываем выходной файл и печатаем в него результат
    output_file = Helper.getFile(output_name, 'w')
    Helper.outputResult(result, output_file)


main('input.txt', 'output.txt')
