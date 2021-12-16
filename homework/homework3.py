def main() -> None:
    """
    Печатает в консоль результат возведения числа в степень

    :rtype: None
    :return: Ничего не возвращает
    """

    # Получаем от пользователя число и степень
    nums = getNumAndPow()

    # Проверяем, что введенные данные - целые числа
    if not checkIntegers(nums):
        printResult('Введены не целые числа')
        exit()

    # Преобразовываем введенные данные в целочисленный тип
    nums = numsStrToInt(nums)
    a, b = tuple(nums)

    # Возводим число в степень и печатаем результат в консоль
    result = Power(a, b)
    result = getMessage(result)
    printResult(result)


def getNumAndPow() -> list:
    """
    Получает из консоли 2 значения

    :rtype: list
    :return: Возвращает список из двух элементов
    """

    a = input('Введите число, возводимое в степень >> ')
    b = input('Введите степень >> ')

    return [a, b]


def checkIntegers(nums: list) -> bool:
    """
    Проверяет список на возможность преобразовать каждый элемент в целое число

    :param nums: Список из строк, содержащих числа
    :type nums: list

    :rtype: bool
    :return: Возвращает истину, если все строки можно преобразовать в целочисленный тип данных.
             В противном случае - ложь
    """

    for num in nums:
        try:
            int(num)
        except ValueError:
            return False

    return True


def numsStrToInt(nums: list) -> list:
    """
    Преобразовывает список из строк, содержащих числа, в список, состоящий из целых чисел

    :param nums: Список из строк, содержащих числа
    :type nums: list

    :rtype: list
    :return: Возвращает список, состоящий из целых чисел
    """

    for i in range(len(nums)):
        nums[i] = int(nums[i])

    return nums


def Power(a: int, b: int) -> int or float or str:
    """
    Возвращает число a в степени b

    :param a: Число, возводимое в степень
    :type a: int
    :param b: Степень, в которую нужно возвести число
    :type b: int

    :rtype: int or float or str
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


def getMessage(result: int or float or str) -> str:
    """
    Преобразовывает результат возведения в степень в сообщение

    :param result: Результат возведения в степень
    :type result: int or float or str

    :rtype: str
    :return: Возвращает текстовое сообщение
    """

    if isinstance(result, str):
        return 'Ошибка >> ' + result

    return 'Результат >> ' + str(result)


def printResult(result: str) -> None:
    """
    Печатает данные в консоль

    :param result: Данные, которые нужно вывести в консоль
    :type result: int or float or str

    :rtype: None
    :return: Ничего не возвращает
    """

    print(result)


main()
