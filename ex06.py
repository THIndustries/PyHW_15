import os
import argparse
import logging
from collections import namedtuple

# логирование.
# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя

"""Этот скрипт пройдет по всем файлам и каталогам в указанной директории (и во всех её поддиректориях),
 создаст для каждого файла или каталога объект FileInfo и запишет информацию о них в файл лога 
 directory_contents.log."""

# Настройка логгирования
logging.basicConfig(filename='directory_contents.log', level=logging.INFO, format='%(message)s')

# Определение namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', 'name extension is_directory parent_directory')

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_info = create_file_info(name, root, False)
            logging.info(file_info)

        for name in dirs:
            dir_info = create_file_info(name, root, True)
            logging.info(dir_info)

def create_file_info(name, root, is_directory):
    if is_directory:
        return FileInfo(name=name, extension=None, is_directory=is_directory,
                        parent_directory=os.path.basename(root))
    else:
        name_without_extension, extension = os.path.splitext(name)
        return FileInfo(name=name_without_extension, extension=extension,
                        is_directory=is_directory, parent_directory=os.path.basename(root))

def main():
    parser = argparse.ArgumentParser(description="Сбор информации о содержимом директории.")
    parser.add_argument("directory", help="Путь до директории")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Указанный путь не является директорией: {args.directory}")
        return

    scan_directory(args.directory)
    print(f"Информация о содержимом директории {args.directory} сохранена в файл "
          f"'directory_contents.log'.")

if __name__ == "__main__":
    main()

