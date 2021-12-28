import datetime
from dateutil import tz

def get_current_date():
    print("Getting Current time.")
    return datetime.date.today()


def get_current_date_and_time():
    print("Getting current date and time.")
    return datetime.datetime.today()


def get_time_in_utc():
    print("Getting time in UTC")
    return datetime.datetime.utcnow()


def get_date_and_time(timezone):
    print("Getting time in {}".format(timezone))
    return datetime.datetime.now(timezone)


def difference_between_datetime(datetime1, datetime2):
    print("Getting difference between {} and {}".format(datetime1, datetime2))
    return datetime1 - datetime2


def get_datetime(years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    print("Getting time by {} years, {} months, {} days, {} hours, {} minutes, {} seconds.".format(years, months, days, hours, minutes, seconds))
    return datetime.datetime(years, months, days, hours, minutes, seconds)


def reduce_datetime(datetime, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    print("Reducing time by {} years, {} months, {} days, {} hours, {} minutes, {} seconds.".format(years, months, days, hours, minutes, seconds))
    return datetime - get_datetime(years, months, days, hours, minutes, seconds)


def convert_datetime_tozone(datetime, timezone):
    print("Converting time to {}".format(timezone))
    return datetime.astimezone(timezone)


today = get_current_date()
print(today)
print(today.isoformat())

now = get_current_date_and_time()
print(now)
print(now.isoformat())
print(convert_datetime_tozone(now, tz.gettz('US/Central')))

datetime1 = get_datetime(1990, 6, 20)
print(datetime1)
print(datetime1.weekday())

if __name__ == "__main__":
    print("Running date time module.....")
else:
    print("Loading Date time module.....")
