# Объединение двух строк с использованием символа `+` называется конкатенацией (concatenation).
# Python поддерживает умножение строк на числа.
hello = "Hello "
world = 'World'

# Получите строку "Hello World" с помощью конкатенации предыдущих переменных
hello_world = hello + world
print(hello_world)

# Получите строку "HelloHelloHelloHelloHelloHelloHelloHelloHelloHello" с помощью операций со строками
many_hello = "Hello" * 10
print(many_hello)

# Получите строку "Hello, World! World World Hello Hello!"  с помощью операций со строками
strange_str = hello.capitalize()[:-1] + ', ' + world + '! ' + world + ' ' + world + ' ' + hello + hello[:-1] + '!'
print(strange_str)

# Вы можете получить доступ к символу строки, если знаете его позицию. Например, str[index] даст символ в позиции index в строке str.
# Запомните! Строки всегда индексируются с 0.

# Используйте переменную python для получения строки "pthn".
python = "Python"
python = python.lower()
p_letter = python[0] + python[2:4] + python[5]
print(p_letter)

# В Python индексы также могут быть отрицательными числами. Это позволяет начать отсчет с конца строки.
# Обратите внимание, что, поскольку -0 совпадает с 0, отрицательные индексы начинаются с -1.
# Таким образом, вы можете использовать отрицательные числа в операторе индексирования для подсчета символов с конца строки.

# Используйте отрицательный индекс для получения символа '!' из строки
long_string = "This is a very long string!"
last_symbol = long_string[-1]
print(last_symbol)
