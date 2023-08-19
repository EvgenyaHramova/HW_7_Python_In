# Создайте функцию, которая создаёт файлы с указанным расширением. 
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

# Чтобы записать байты можно использовать список с числами и функцию bytes

from random import randint
import random
import string

def file_generator(expansion_, min_len_name, max_len_name, min_bytes, max_bytes, count_files):
    count_ = 0
    while count_ < count_files:
        name_file = ''
        for _ in range(randint(min_len_name, max_len_name)):
            name_file += name_file.join(random.choice(string.ascii_lowercase))
        with open(name_file + expansion_, 'w') as f:
            for _ in range(randint(min_bytes, max_bytes)):
                text = bytes(randint(1, 50))
                f.write(str(text)+'\n')
        count_ += 1 
   
    

if __name__ == '__main__':
    expansion_ = '.txt'
    min_len_name = 6
    max_len_name = 15
    min_bytes = 256
    max_bytes = 1256
    count_files = 3
    file_generator(expansion_, min_len_name, max_len_name, min_bytes, max_bytes, count_files)