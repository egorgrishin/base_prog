from datetime import datetime

def getPointsCount(coordinates, radius):
    """
    Считает количество точек с целочисленными координатами в окружности используя формулу расстояния между точек
    """

    coordinates = list(map(int, coordinates))
    radius = int(radius)

    x = coordinates[0] - radius
    y = coordinates[1] - radius
    points_count = 0

    for i in range(y, y + 2 * radius + 1):
        for n in range(x, x + 2 * radius + 1):
            if getPointsDistance(coordinates[0], n, coordinates[1], i) <= radius:
                points_count += 1

    return str(points_count)


def getPointsDistance(x, x0, y, y0):
    return ((x0 - x) ** 2 + (y0 - y) ** 2) ** 0.5


def getResult(data, first_datetime):
    result = f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\n{data}\n"
    result += str(datetime.timestamp(datetime.now()) - datetime.timestamp(first_datetime))
    return result