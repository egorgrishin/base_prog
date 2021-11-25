import lab6.helper as Helper


def main(input_name, output_name):
    input_file = Helper.getFile(input_name)
    if not input_file:
        print('Файл с входными данными не обнаружен')
        return False

    max_number = input_file.readline()
    input_file.close()
    if not Helper.isNumber(max_number):
        print('В файле указаны некорректные данные')
        return False

    elementary_nums = getElementaryNumbers(max_number)

    output_file = Helper.getFile(output_name, 'w')
    Helper.outputResult(elementary_nums, output_file)


def getElementaryNumbers(max_number):
    max_number = int(max_number)
    numbers_set = set(range(2, max_number + 1))
    elementary_nums = ''

    while numbers_set:
        min_number = min(numbers_set)
        elementary_nums += str(min_number) + ' '
        numbers_set -= set(range(min_number, max_number + 1, min_number))

    return elementary_nums


main('input.txt', 'output.txt')
