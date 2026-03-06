from datetime import datetime, timezone, timedelta

def parse_moment(line):
    date_part, utc_part = line.split()
    
    sign = 1 if '+' in utc_part else -1
    hours, minutes = map(int, utc_part[4:].split(':'))
    
    offset = timedelta(hours=hours, minutes=minutes) * sign
    tz = timezone(offset)
    
    dt = datetime.strptime(date_part, '%Y-%m-%d')
    return dt.replace(tzinfo=tz)

dt1 = parse_moment(input().strip())
dt2 = parse_moment(input().strip())

diff = abs((dt1 - dt2).total_seconds())
print(int(diff // 86400))