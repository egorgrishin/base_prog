import os


def getFile(file, mode='r'):
    file_list = os.listdir()

    if not checkFile(file) and mode == 'r':
        return False

    return open(file, mode)


def checkFile(file):
    return os.path.exists(file)


def outputResult(result, file):
    file.write(result)
    file.close()


def isNumber(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def isNumbersList(numbers):
    for number in numbers:
        if not isNumber(number):
            return False

    return True


def roundMatrix(matrix, digits):
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            matrix[i][k] = round(matrix[i][k], 2)

    return matrix