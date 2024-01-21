import logging
import functools

# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

logging.basicConfig(filename='logg_from_decorator.log', encoding='utf-8', level=logging.INFO)
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
