""" НОД """


def getNod(a, b):
    """ Возвращает наибольший общий делитель """
    if b == 0:
        return abs(a)
    return getNod(b, a % b)


numbers = list(map(int, input('Введите 2 числа >> ').split()))
print(getNod(numbers[0], numbers[1]))