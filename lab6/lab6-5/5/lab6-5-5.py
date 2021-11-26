import lab6.helper as Helper
import numpy


def main(input_name, output_name):
    input_file = Helper.getFile(input_name)
    if not input_file:
        print('Файл с входными данными не обнаружен')
        return False

    size = input_file.readline().split()
    if not Helper.isNumbersList(size) or len(size) != 2:
        print('В файле указаны некорректные данные')
        return False

    matrix_a = getMatrix(size, 0, 10)
    matrix_a = Helper.roundMatrix(matrix_a / matrix_a.max(), 2)
    matrix_b = getMatrix([size[1], numpy.random.randint(5, 16)], 0, 10)
    multiple = Helper.roundMatrix(numpy.dot(matrix_a, matrix_b), 2)
    result = getOutput(matrix_a, matrix_b, multiple)

    output_file = Helper.getFile(output_name, 'w')
    Helper.outputResult(result, output_file)


def getMatrix(size, min_val, max_val):
    size = list(map(int, size))
    return numpy.random.randint(min_val, max_val + 1, size)


def getOutput(matrix_a, matrix_b, multiple):
    result = 'Matrix A:\n'
    for i in matrix_a:
        for n in i:
            result += str(n) + ' '
        result += '\n'

    result += '\nMatrix B:\n'
    for i in matrix_b:
        for n in i:
            result += str(n) + ' '
        result += '\n'

    result += '\nMatrix A*B:\n'
    for i in multiple:
        for n in i:
            result += str(n) + ' '
        result += '\n'

    return result


main('input.txt', 'output.txt')
