import logging
# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

logging.basicConfig(filename='my_logger.log', filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)
def division_func(*, num1: int, num2:int)-> float:
    result = num1 / num2
    return result

if __name__ == '__main__':
    num1, num2 = int(input('Введите делимое число: ')), int(input('Введите делитель: '))
    try:
        res = division_func(num1=num1, num2=num2)
    except ZeroDivisionError as e:
        logger.error(f'Пытаетесь поделить {num1} на {num2}. {e}')
    else:
        print(res)