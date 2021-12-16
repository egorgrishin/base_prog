def Power(a, b):
    """
    Возвращает число a в степени b

    :param a: Число, возводимое в степень
    :type a: int
    :param b: Степень, в которую нужно возвести число
    :type b: int

    :rtype: int or float
    :return: Возвращает число a в степени b
    """
    if b == 0:
        return 1
    elif b > 0:
        return a * Power(a, b - 1)
    elif a != 0:
        return 1 / a * Power(a, b + 1)
    else:
        return 'Ноль нельзя возводить в отрицательную степень'


print(Power(10**1000, 997))
