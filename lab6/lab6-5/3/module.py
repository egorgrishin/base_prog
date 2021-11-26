def getElementaryNumbers(max_number):
    max_number = int(max_number)
    # Составляем множество начиная с 2 до максимального числа
    numbers_set = set(range(2, max_number + 1))
    elementary_nums = ''

    while numbers_set:
        # Получаем минимальное число из множества
        min_number = min(numbers_set)
        # Записываем это число
        elementary_nums += str(min_number) + ' '
        # Вычитаем из начального множества множество, начиная с min_number с шагом min_number до максимального числа
        numbers_set -= set(range(min_number, max_number + 1, min_number))

    return elementary_nums
