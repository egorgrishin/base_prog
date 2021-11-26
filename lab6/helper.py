import os


def getFile(file, mode='r'):
    # Получаем список файлов в директории
    file_list = os.listdir()

    # Проверяем наличие файла и открываем его
    if not checkFile(file) and mode == 'r':
        return False

    return open(file, mode)


def checkFile(file):
    # Проверяем наличие файла
    return os.path.exists(file)


def outputResult(result, file):
    # Печатаем результат и закрываем файл
    file.write(result)
    file.close()


def isNumber(number):
    # Проверяем что number - строка, содержащая числа
    try:
        int(number)
        return True
    except ValueError:
        return False


def isNumbersList(numbers):
    # Проверяем что numbers - список строк, содержащих числа
    for number in numbers:
        if not isNumber(number):
            return False

    return True


def roundMatrix(matrix, digits):
    # Округляем каждое значение матрицы
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            matrix[i][k] = round(matrix[i][k], digits)

    return matrix
