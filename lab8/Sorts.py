import random


def sortBubble(a: list, reverse=False) -> list:
    """ Обменная сортировка """

    if reverse:
        for i in range(len(a)):
            for n in range(len(a) - 2, i - 1, -1):
                if a[n + 1] > a[n]:
                    a[n + 1], a[n] = a[n], a[n + 1]
    else:
        for i in range(len(a)):
            for n in range(len(a) - 1, i - 1, -1):
                if a[n - 1] > a[n]:
                    a[n - 1], a[n] = a[n], a[n - 1]

    return a


def sortSelect(a: list, reverse=False) -> list:
    """ Сортировка выбором """

    if reverse:
        for i in range(len(a)):
            i_min = i

            for j in range(i + 1, len(a)):
                if a[j] > a[i_min]:
                    i_min = j

            a[i], a[i_min] = a[i_min], a[i]
    else:
        for i in range(len(a)):
            i_min = i

            for j in range(i + 1, len(a)):
                if a[j] < a[i_min]:
                    i_min = j

            a[i], a[i_min] = a[i_min], a[i]

    return a


def sortQuick(a: list) -> list:
    """ Быстрая сортировка """

    if len(a) <= 1:
        return a

    rand_elem = random.choice(a)

    left_nums = [n for n in a if n < rand_elem]
    center_nums = [rand_elem] * a.count(rand_elem)
    right_nums = [n for n in a if n > rand_elem]

    return sortQuick(left_nums) + center_nums + sortQuick(right_nums)
