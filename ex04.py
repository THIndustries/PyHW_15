import datetime
import re
import logging

# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.


# Настройка логгирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_date(text):
    # Словарь для преобразования месяцев
    months = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12
    }

    # Словарь для преобразования дней недели
    days = {
        'понедельник': 0,
        'вторник': 1,
        'среда': 2,
        'четверг': 3,
        'пятница': 4,
        'суббота': 5,
        'воскресенье': 6
    }

    # Регулярное выражение для разбора строки
    match = re.match(r'(\d+)-[а-я]{1,2}\s([а-я]+)\s([а-я]+)', text)
    if not match:
        logging.error(f"Строка '{text}' не соответствует формату")
        return None

    week_number, day_of_week, month = match.groups()

    try:
        week_number = int(week_number)
        day_of_week_num = days[day_of_week]
        month_num = months[month]
    except KeyError as e:
        logging.error(f"Ошибка в названии дня или месяца: {e}")
        return None
    except ValueError:
        logging.error("Ошибка в преобразовании номера недели")
        return None

    # Нахождение соответствующей даты
    date = datetime.datetime(datetime.datetime.now().year, month_num, 1)
    while date.weekday() != day_of_week_num:
        date += datetime.timedelta(days=1)

    # Переход к нужной неделе
    date += datetime.timedelta(weeks=week_number - 1)

    return date

# Пример использования
print(parse_date("1-й четверг ноября"))
print(parse_date("43534"))

