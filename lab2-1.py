a = b = 2  # Пример множественного оператора присваивания.
# Обратите внимание на значения переменных a и b после выполнения данной операции.

print("a = " + str(a))  # Функция str() используется для приведения типа аргумента к строковому
print("b = " + "str(b)")

hello = "Привет"
print("hello = " + str(hello))

# Переопределите значение переменной hello
hello = 'Hi'
print("hello = " + str(hello))

# Создайте ещё несколько переменных, а затем осуществите их вывод через пробел
fingers_count, is_student, middle_score = 5, bool('1'), float(4)
print(fingers_count, is_student, middle_score)
