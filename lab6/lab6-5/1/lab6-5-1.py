import lab6.helper as Helper
from rectangle import printRectangle
from square import printSquare


def main(input_name):
    input_file = Helper.getFile(input_name)
    if not input_file:
        print('Файл с входными данными не обнаружен')
        return False

    params = input_file.readline().split()
    params = list(map(int, params))
    output_file = Helper.getFile(input_file.readline(), 'w')
    input_file.close()

    if len(params) == 2:
        printRectangle(params[0], params[1], output_file)
    else:
        printSquare(params[0], output_file)


main('input.txt')
