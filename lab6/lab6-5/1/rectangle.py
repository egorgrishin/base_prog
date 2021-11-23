def printRectangle(a, b, file):
    rectangle = ''
    for i in range(b):
        if i == 0 or i == b - 1:
            rectangle += '*' * a + '\n'
        else:
            rectangle += '*' + ' ' * (a - 2) + '*' + '\n'
    f = open(file, 'w')
    f.write(rectangle)
    f.close()

