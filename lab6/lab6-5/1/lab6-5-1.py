import lab6.helper as Helper
import module as Figure


def main(input_name):
    # Открываем файл, если он имеется
    input_file = Helper.getFile(input_name)
    if not input_file:
        print('Файл с входными данными не обнаружен')
        return False

    # Получаем размеры и проверяем их
    size = input_file.readline().split()
    if not Helper.isNumbersList(size) or len(size) != 2:
        print('В файле указаны некорректные данные')
        return False
    size = list(map(int, size))

    # Открываем файл для записи и закрываем файл с входными данными
    output_file = Helper.getFile(input_file.readline(), 'w')
    input_file.close()

    # Исходя из входных данных печатаем квадрат либо прямоугольник
    if len(size) == 2:
        Figure.printRectangle(size[0], size[1], output_file)
    else:
        Figure.printSquare(size[0], output_file)


main('input.txt')
