import os
from datetime import datetime, timedelta

#  Если подниматься много раз, то бывают случаи, когда, например, через цикл  делают? А то не красиво как на 5 строке.
eugene_okulik_directory_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_okulik_file_path = os.path.join(eugene_okulik_directory_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(eugene_okulik_file_path, encoding='utf-8') as okulik_file:
    # print(okulik_file.read())   # для себя
    dates = []
    for line in okulik_file:
        old_date = datetime.strptime(line.split(' - ')[0].split('. ')[1], '%Y-%m-%d %H:%M:%S.%f')
        dates.append(old_date)


def add_week(date):
    return f'Дата на неделю позже: {date + timedelta(weeks=1)}'


def show_day_of_week(date):
    return f'День недели: {date.strftime("%A")}'


def count_days_ago(date):
    return f'Cколько дней назад была эта дата: {(datetime.now() - date).days}'


print(add_week(dates[0]))
print(show_day_of_week(dates[1]))
print(count_days_ago(dates[2]))
