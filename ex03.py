import logging
import functools
import datetime

# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

logging.basicConfig(filename='function.log', level=logging.INFO, encoding='utf-8',
                    format='%(levelname)s %(asctime)s - %(funcName)s - %(message)s')
logger = logging.getLogger(__name__)


def log_func(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        logger.info(f'Вызов функции {func.__name__} c аргументами {args} и {kwargs}')
        res = func(*args, **kwargs)
        logger.info(f'Функция {func.__name__} возвращает результат: {res}')
        return res

    return inner_func

@log_func
def find_sum(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(find_sum(3, 9))
