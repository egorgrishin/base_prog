"""
Python имеет ряд встроенных функций для чтения и записи информации из файла на вашем компьютере.
Функция open используется для открытия файла.
Файл можно открыть в режиме чтения (используя «r» в качестве второго аргумента) или в режиме записи (используя «w» в качестве второго аргумента).
Функция open возвращает объект файла. Вам нужно сохранить его, чтобы закрыть файл позже.
"""

# Создайте в папке с проектом файлы input.txt и input1.txt
f = open("input.txt", "r")   # здесь мы открываем файл "input.txt"
# Второй аргумент используется для определения режима работы с файлом (в данном случае - чтение из файла)
# Примечание: если вы хотите записывать в файл, используйте «w» в качестве второго аргумента


# Выведите содержимое «input.txt». Выведите первую строку «input1.txt». Затем закройте файлы.
for line in f.readlines():
    print(line) # выведите каждую строку
f.close() # Важно закрыть файл, чтобы освободить системные ресурсы.

f1 = open("input1.txt", "r")
print(f1.readline())
f.close()
# выведите только первую строку input1.txt. Не забудьте закрыть файл


# ---------------------------------------------------------#


""" Если вы откроете файл, используя «w» в качестве второго аргумента (на запись), будет создан новый пустой файл. 
Обратите внимание, что если существует другой файл с таким же именем, он будет удален. 
Если вы хотите добавить какой-либо контент в существующий файл, вы должны использовать модификатор «a» (добавление). 
"""

zoo = ['lion', "elephant", 'monkey']

# Добавьте элементы списка zoo в файл "output.txt"

print(__name__)
if __name__ == "__main__":
    f = open("output.txt", 'a') # добавьте нужный аргумент
    for i in zoo:
        f.write(f"{i}\n") # добавьте все элементы в файл

f.close()
# закройте файл
