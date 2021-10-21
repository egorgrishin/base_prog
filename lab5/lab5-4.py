def main():
    """Контроллер функций треугольника"""

    parties = get_parties()

    if not check_existence(parties):
        return 'Треугольник не существует'

    return get_type(parties)


def get_parties():
    """Получает длины сторон треугольника"""

    parties = []

    for i in range(3):
        parties.append(float(input(f'Длина стороны {i + 1}: ')))

    return parties


def check_existence(parties):
    """Проверяет существование треугольника"""

    c = parties.index(max(parties))
    a = (4 + c) % 3
    b = (5 + c) % 3

    if parties[c] < (parties[a] + parties[b]) and parties[a] > 0 and parties[b] > 0 and parties[c] > 0:
        return True
    else:
        return False


def get_type(parties):
    """Возвращает вид треугольника"""

    if parties[0] == parties[1] == parties[2]:
        return 'Треугольник равносторонний'
    elif parties[0] == parties[1] or parties[1] == parties[2] or parties[2] == parties[0]:
        return 'Треугольник равнобедренный'
    else:
        return 'Треугольник общего вида'


# Main program
print(main())
