import datetime
import logging
import argparse

# Настройка логгирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_date(week_number, day_of_week, month):
    # Словарь для преобразования месяцев
    months = {
        'январь': 1, '1': 1,
        'февраль': 2, '2': 2,
        'март': 3, '3': 3,
        'апрель': 4, '4': 4,
        'май': 5, '5': 5,
        'июнь': 6, '6': 6,
        'июль': 7, '7': 7,
        'август': 8, '8': 8,
        'сентябрь': 9, '9': 9,
        'октябрь': 10, '10': 10,
        'ноябрь': 11, '11': 11,
        'декабрь': 12, '12': 12
    }

    # Словарь для преобразования дней недели
    days = {
        'понедельник': 0, '1': 0,
        'вторник': 1, '2': 1,
        'среда': 2, '3': 2,
        'четверг': 3, '4': 3,
        'пятница': 4, '5': 4,
        'суббота': 5, '6': 5,
        'воскресенье': 6, '7': 6
    }

    try:
        week_number = int(week_number) if week_number else 1
        day_of_week_num = days.get(day_of_week.lower(), datetime.datetime.now().weekday()) if day_of_week else datetime.datetime.now().weekday()
        month_num = months.get(month.lower(), datetime.datetime.now().month) if month else datetime.datetime.now().month
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

def main():
    parser = argparse.ArgumentParser(description="Преобразование даты из текстового формата.")
    parser.add_argument("-w", "--week", help="Номер недели (1-й, 2-й, ...)", default=None)
    parser.add_argument("-d", "--day", help="День недели (понедельник, вторник, ... или 1, 2, ...)", default=None)
    parser.add_argument("-m", "--month", help="Месяц (январь, февраль, ... или 1, 2, ...)", default=None)

    args = parser.parse_args()

    date = parse_date(args.week, args.day, args.month)
    if date:
        print(f"Рассчитанная дата: {date.strftime('%Y-%m-%d')}")
    else:
        print("Не удалось рассчитать дату.")

if __name__ == "__main__":
    main()
