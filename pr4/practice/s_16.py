from datetime import datetime, timezone, timedelta

def parse_moment(line):
    date_part, time_part, utc_part = line.split()
    
    sign = 1 if utc_part[3] == '+' else -1
    hours, minutes = map(int, utc_part[4:].split(':'))
    
    tz = timezone(timedelta(hours=hours, minutes=minutes) * sign)
    dt = datetime.strptime(date_part + " " + time_part, "%Y-%m-%d %H:%M:%S")
    
    return dt.replace(tzinfo=tz)

start = parse_moment(input().strip())
end = parse_moment(input().strip())
duration = (end - start).total_seconds()
print(int(duration))