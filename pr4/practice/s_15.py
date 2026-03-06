from datetime import datetime, timezone, timedelta
import math

def parse_moment(line):
    d, u = line.split()
    sign = 1 if u[3] == '+' else -1
    h, m = map(int, u[4:].split(':'))
    tz = timezone(timedelta(hours=h, minutes=m) * sign)
    return datetime.strptime(d, '%Y-%m-%d').replace(tzinfo=tz)

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

birth = parse_moment(input().strip())
current = parse_moment(input().strip())

def build_birthday(year):
    day = birth.day
    if birth.month == 2 and birth.day == 29 and not is_leap(year):
        day = 28
    return datetime(year, birth.month, day, tzinfo=birth.tzinfo)

year = current.year
next_birthday = build_birthday(year)

if next_birthday < current:
    next_birthday = build_birthday(year + 1)

diff_seconds = (next_birthday - current).total_seconds()

# округляем вверх, если есть остаток
days = math.ceil(diff_seconds / 86400)

print(days)