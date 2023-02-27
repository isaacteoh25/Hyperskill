from datetime import datetime

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]
# def get_weekday(datetime_obj):
#     return weekdays[datetime_obj.weekday()]

def get_weekday(datetime_obj):
    return datetime_obj.strftime("%A")
date_string = "06/04/2020 12:30"

# date = "1611-12-24 16:30"
date = "Day of release: 4 July 2019"
dt1 = datetime.strptime(date_string, "%m/%d/%Y %H:%M")
a = date.split(":", 1)
# dt2 = datetime.strptime(date, "%Y-%m-%d %H:%M")
dt2 = datetime.strptime(a[1], "%d %B %Y")
print(dt2.strftime("%Y-%m-%d"))
print((dt2.strftime("%Y-%m-%d %H:%M:%S")))
print(get_weekday(dt1))
print(get_weekday(datetime.today()))

def get_release_date(release_str):
    # return datetime.strptime(release_str, "Day of release: %d %B %Y")
    # return datetime.strptime(release_str.split(sep=': ')[1], "%d %B %Y")
    # return datetime.strptime(release_str[16:], "%d %B %Y")
    return datetime.strptime(release_str.replace('Day of release: ', ''), "%d %B %Y")

print(get_release_date("Day of release: 4 July 2019"))