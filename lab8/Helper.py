from prettytable import PrettyTable
import os


def getResultTable(data) -> str:
    """ Создает результирующую таблицу измерений для различных методов сортировки """

    # Преобразовываем данные для таблицы
    table_data = getTableData(data)

    # Создаем таблицу и заполняем ее данными
    table = PrettyTable()
    table.field_names = ["Метод", "Отсортированная", "Случайная", "Отсортированная в обратном порядке"]
    table.add_rows(table_data)

    # Возвращаем таблицу в виде строки
    return table.get_string()


def getTableData(data) -> list:
    """ Возвращает данные для таблицы. Убирает из списков функции """

    result = []

    for item in data:
        result += [item[1:]]

    return result


def writeResultTable(table, output_name) -> None:
    """ Записывает данные в файл """

    output_file = getFile(output_name, 'w')
    output_file.write(table)
    output_file.close()


def getFile(file, mode='r'):
    """ Возвращает открытый файл в указанном режиме """

    # Проверяем наличие файла и открываем его
    if not checkFile(file) and mode == 'r':
        return False

    return open(file, mode)


def checkFile(file) -> bool:
    """ Проверяет существование файла в директории """

    return os.path.exists(file)


def check(a: list):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False

    return True
