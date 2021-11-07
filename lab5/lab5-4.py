def triangle():
    """Контроллер функций треугольника"""

    data = get_parties()

    if not data['status']:
        return 'Треугольник не существует'
    parties = data['parties']

    if not check_existence(parties):
        return 'Треугольник не существует'

    return get_type(parties)


def get_parties():
    """Получает длины сторон треугольника"""

    parties = []

    for i in range(3):
        part = input(f'Длина стороны {i + 1}: ')

        if not is_number(part):
            return {'status': False}

        parties.append(float(part))

    return {
        'status': True,
        'parties': parties
    }


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


def is_number(part):
    """Проверяет, можно ли преобразовать строку в вещественное число"""

    try:
        float(part)
        return True
    except ValueError:
        return False


def equation():
    """Контроллер решений квадратного уравнения"""

    data = get_factors()
    if not data['status']:
        return 'Некорекктные коэффициенты уравнения'

    factors = data['factors']
    print(f'Уравнение: ({factors[0]})*X^2 + ({factors[1]})*X + ({factors[2]}))')

    solutions = get_solutions(factors)
    print(f'Количество корней: {len(solutions)}')

    if len(solutions) > 0:
        for i in solutions:
            print(i)


def get_factors():
    """Получает коэффициенты квадратного уравнения с клавиатуры"""

    a = input('Введите коэфициент A: ')
    b = input('Введите коэфициент B: ')
    c = input('Введите коэфициент C: ')
    factors = [a, b, c]

    for factor in factors:
        if not is_number(factor):
            return {'status': False}

    if factors[0] == 0:
        return {'status': False}

    return {
        'status': True,
        'factors': list(map(float, factors)),
    }


def get_solutions(factors):
    """Возвращает массив решений квадратного уравнения"""

    d = factors[1] ** 2 + (-4 * factors[0] * factors[2])
    solutions = []

    if d > 0:
        solutions.append((-factors[1] + d ** 0.5) / (2 * factors[0]))
        solutions.append((-factors[1] - d ** 0.5) / (2 * factors[0]))
    elif d == 0:
        solutions.append(-factors[1] / (2 * factors[0]))

    return solutions


def arrival_time():
    """Контроллер нахождения времени прибытия поезда"""

    data = get_times()
    if not data['status']:
        return 'Некорекктные коэффициенты уравнения'

    times = count_time(data['times'])
    print(f"{times['hours']} hours : {times['minutes']} minutes : {times['days']} days")



def get_times():
    """Получает время отправление и время в пути поезда"""

    times = [
        input('Время отправления поезда (в часах): '),
        input('Время отправления поезда (в минутах): '),
        input('Время поезда в пути (в часах): '),
        input('Время поезда в пути (в минутах): '),
    ]

    for time in times:
        if not time.isdigit():
            return {'status': False}

    return {
        'status': True,
        'times': list(map(int, times)),
    }


def count_time(times):
    """Считает, сколько времени поезд провел в пути"""

    add_hours = 0
    result = {
        'minutes': 0,
        'hours': 0,
        'days': 0,
    }

    tmp = times[3] + times[1]
    add_hours += tmp // 60
    result['minutes'] = str(tmp % 60)
    if len(result['minutes']) < 2:
        result['minutes'] = '0' + result['minutes']

    tmp = times[2] + times[0]
    result['hours'] = str(tmp % 24 + add_hours)
    if len(result['hours']) < 2:
        result['hours'] = '0' + result['hours']
    result['days'] = str(times[2] // 24)

    return result


# Main program
print(triangle())
equation()
arrival_time()
