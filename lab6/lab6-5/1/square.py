def printSquare(a, output_file):
    rectangle = ''

    for i in range(a):
        if i == 0 or i == a - 1:
            rectangle += '*' * a + '\n'
        else:
            rectangle += '*' + ' ' * (a - 2) + '*' + '\n'

    output_file.write(rectangle)
    output_file.close()