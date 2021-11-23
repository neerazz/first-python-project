"""
Ann watched a TV program about health and learned that it is recommended to sleep at least A hours per day,
but oversleeping is also not healthy, and you should not sleep more than B hours. Now Ann sleeps H hours per day.
If Ann's sleep schedule complies with the requirements of that TV program – print "Normal".
If Ann sleeps less than A hours, output “Deficiency”, and if she sleeps more than B hours, output “Excess”.
"""


def check_healthy_sleep(a, b, h):
    if h < a:
        print("Deficiency")
    elif a <= h <= b:
        print("Normal")
    else:
        print("Excess")


def check_leap_year(year):
    divided_by_4 = is_divisible_by(year, 4)
    divided_by_100 = is_divisible_by(year, 100)
    divided_by_400 = is_divisible_by(year, 400)
    if divided_by_4:
        if divided_by_100:
            if divided_by_400:
                return True
        else:
            return True
    else:
        return False


def is_divisible_by(num, div):
    return num % div == 0


print("Leap" if check_leap_year(2000) else "Ordinary")
print("Leap" if check_leap_year(2100) else "Ordinary")
print("Leap" if check_leap_year(2008) else "Ordinary")
