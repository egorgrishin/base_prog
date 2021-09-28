import statistics
# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9
print(type(number))   # Вывод типа переменной number

float_number = int(9.0)
print(float_number, type(float_number))

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов
year, age, price, name, my_scores, is_successful = str(2003), int('18'), float(39), 'Егор', [2, 3, 4, 5], False

if int(statistics.mean(my_scores)) >= 3:
    is_successful = True

print(type(year), type(age), type(price), type(name), type(my_scores), type(is_successful))

# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.