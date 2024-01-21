import os
import sys
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, filename='rename_files.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

def rename_files(desired_name, num_digits, source_ext, target_ext, folder_name, name_range=None):
    new_names = []

    try:
        # Получаем список файлов в указанной директории
        files = os.listdir(folder_name)

        # Фильтруем только нужные файлы с указанным расширением
        filtered_files = [file for file in files if file.endswith(source_ext)]

        # Сортируем файлы по имени
        filtered_files.sort()

        # Задаем начальный номер для порядкового номера
        num = 1

        # Переименовываем файлы
        for file in filtered_files:
            # Получаем имя файла без расширения
            name = os.path.splitext(file)[0]

            # Если задан диапазон, обрезаем имя файла
            if name_range:
                name = name[name_range[0]-1:name_range[1]]

            # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
            new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

            # Переименовываем файл
            path_old = os.path.join(os.getcwd(), folder_name, file)
            path_new = os.path.join(os.getcwd(), folder_name, new_name)
            os.rename(path_old, path_new)

            # Добавляем новое имя в список
            new_names.append(new_name)

            # Увеличиваем порядковый номер
            num += 1

        logging.info("Файлы успешно переименованы: %s", new_names)

    except Exception as e:
        logging.error("Ошибка при переименовании файлов: %s", str(e))

if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Недостаточно аргументов. Использование: python script.py "
              "[желаемое_имя] [число_цифр] [исходное_расширение] [целевое_расширение] [имя_папки]")
        logging.info("Недостаточно аргументов")
    else:
        desired_name = sys.argv[1]
        num_digits = int(sys.argv[2])
        source_ext = sys.argv[3]
        target_ext = sys.argv[4]
        folder_name = sys.argv[5]
        name_range = None
        if len(sys.argv) > 6:
            range_start, range_end = map(int, sys.argv[6].split(','))
            name_range = (range_start, range_end)

        rename_files(desired_name, num_digits, source_ext, target_ext, folder_name, name_range)
