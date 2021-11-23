def printSquare(a, file):
    rectangle = ''
    for i in range(a):
        if i == 0 or i == a - 1:
            rectangle += '*' * a + '\n'
        else:
            rectangle += '*' + ' ' * (a - 2) + '*' + '\n'
    f = open(file, 'w')
    f.write(rectangle)
    f.close()