max_number = int(input("Введите верхнюю границу диапазона: "))
numbers_set = set(range(2, max_number + 1))
while numbers_set:
    min_number = min(numbers_set)
    print(min_number)
    numbers_set -= set(range(min_number, max_number + 1, min_number))