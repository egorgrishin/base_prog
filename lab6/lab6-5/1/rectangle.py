def printRectangle(a, b, output_file):
    rectangle = ''

    for i in range(b):
        if i == 0 or i == b - 1:
            rectangle += '*' * a + '\n'
        else:
            rectangle += '*' + ' ' * (a - 2) + '*' + '\n'

    output_file.write(rectangle)
    output_file.close()

