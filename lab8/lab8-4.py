from time import process_time as timer
from random import randint
import Sorts
import Helper


def main(output_name: str) -> None:
    """ Производит измерения скорости различных функций сортировки и записывает их в файл в виде таблицы """

    # Список с функциями сортировки и их названиями
    sorter = [
        [Sorts.sortBubble, 'Обменная сортировка'],
        [Sorts.sortSelect, 'Сортировка выбором'],
        [Sorts.sortQuick, 'Быстрая сортировка'],
        [sorted, 'Встроенная функция']
    ]

    # Получаем последовательности
    sequences = getSequences()

    # Производим сортировки с учетом времени выполнения
    sorter = makeSorts(sorter, sequences)

    # Получаем результирующую таблицу
    table = Helper.getResultTable(sorter)

    # Записываем результирующую таблицу в файл
    Helper.writeResultTable(table, output_name)


def makeSorts(sorter: list, sequences: list) -> list:
    """ Производит сортировки с учетом их времени выполнения """
    for sequence in sequences:
        for sort in sorter:
            sequence_copy = sequence.copy()

            # Записываем длительность выполнения сортировки в соответствующий ей элемент списка
            sort += [sortSequenceWithTimer(sequence_copy, sort[0])]

    return sorter


def getSequences() -> list:
    """ Возвращает случайную, отсортированную и обратно отсортированную последовательности из N целых чисел """

    n = int(input('Количество элементов последовательности >> '))
    template = [randint(0, 100) for _ in range(n)]

    return [
        sorted(template),
        template,
        sorted(template, reverse=True),
    ]


def sortSequenceWithTimer(sequence, sort_func) -> float:
    """ Производит сортировку с учетом времени выполнения """

    time_start = timer()
    sort_func(sequence)
    time_end = timer()

    return time_end - time_start


main('output.txt')
