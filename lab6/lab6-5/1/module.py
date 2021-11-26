def printRectangle(a, b, output_file):
    rectangle = ''
    # Заполняем переменную рисунком
    for i in range(b):
        if i == 0 or i == b - 1:
            rectangle += '*' * a + '\n'
        else:
            rectangle += '*' + ' ' * (a - 2) + '*' + '\n'

    # Печатаем рисунок в файл и закрываем его
    output_file.write(rectangle)
    output_file.close()


def printSquare(a, output_file):
    rectangle = ''
    # Заполняем переменную рисунком
    for i in range(a):
        if i == 0 or i == a - 1:
            rectangle += '*' * a + '\n'
        else:
            rectangle += '*' + ' ' * (a - 2) + '*' + '\n'

    # Печатаем рисунок в файл и закрываем его
    output_file.write(rectangle)
    output_file.close()
