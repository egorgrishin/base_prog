""" Получить из 1 число N """


def plusFive(current, target):
    """ Прибавляет к текущему числу 5 """
    current += 5
    if current == target:
        return True
    elif current > target:
        return False
    return True if plusThree(current, target) or plusFive(current, target) else False


def plusThree(current, target):
    """ Прибавляет к текущему числу 3 """
    current += 3
    if current == target:
        return True
    elif current > target:
        return False
    return True if plusThree(current, target) or plusFive(current, target) else False


target = int(input('Введите число N >> '))
print('YES' if plusThree(1, target) or plusFive(1, target) or target == 1 else 'NO')
