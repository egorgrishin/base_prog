from rectangle import printRectangle
from square import printSquare


def main():
    f = open('input.txt')
    params = f.readline().split()
    params = list(map(int, params))
    file = f.readline()
    print(params, file)
    if len(params) == 2:
        printRectangle(params[0], params[1], 'output.txt')
    else:
        printSquare(params[0], 'output.txt')


main()
