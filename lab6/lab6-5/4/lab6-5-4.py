import lab6.helper as Helper


def main(input_name, output_name):
    input_file = Helper.getFile(input_name)
    if not input_file:
        print('Файл с входными данными не обнаружен')
        return False

    radius = input_file.readline()
    if not Helper.isNumber(radius):
        print('В файле указаны некорректные данные')
        return False

    coordinates = input_file.readline().split()
    if not Helper.isNumbersList(coordinates) or len(coordinates) != 2:
        print('В файле указаны некорректные данные')
        return False

    points_count = getPointsCount(coordinates, radius)

    output_file = Helper.getFile(output_name, 'w')
    Helper.outputResult(points_count, output_file)


def getPointsCount(coordinates, radius):
    coordinates = list(map(int, coordinates))
    radius = int(radius)

    x = coordinates[0] - radius
    y = coordinates[1] - radius
    points_count = 0

    for i in range(y, y + 2 * radius + 1):
        for n in range(x, x + 2 * radius + 1):
            if getPointsDistance(coordinates[0], n, coordinates[1], i) <= radius:
                points_count += 1

    return str(points_count)


def getPointsDistance(x, x0, y, y0):
    return ((x0 - x) ** 2 + (y0 - y) ** 2) ** 0.5


main('input.txt', 'output.txt')