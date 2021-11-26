import lab6.helper as Helper
import module as Module


def main(input_name, output_name):
    # Проверяем наличие файла и открываем его
    input_file = Helper.getFile(input_name)
    if not input_file:
        print('Файл с входными данными не обнаружен')
        return False

    # Читаем данные и проверяем их
    max_number = input_file.readline()
    input_file.close()
    if not Helper.isNumber(max_number):
        print('В файле указаны некорректные данные')
        return False

    # Список простых чисел от 2 до max_number
    elementary_nums = Module.getElementaryNumbers(max_number)

    # Открываем выходной файл и печатаем в него результат
    output_file = Helper.getFile(output_name, 'w')
    Helper.outputResult(elementary_nums, output_file)


main('input.txt', 'output.txt')
