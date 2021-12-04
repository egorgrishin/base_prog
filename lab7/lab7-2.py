""" N-е число Фибоначчи """


def getFib(current, prev, step, target):
    """ Возвращает заданное число Фибоначчи """
    if step == target or target == 1:
        return current + prev
    else:
        return getFib(current + prev, current, step + 1, target)


target = int(input('Введите номер числа Фибоначчи >> '))
print(getFib(1, 0, 2, target))