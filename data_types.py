number = 1

print(number)
print(type(number))

decimal = 1.3

print(decimal)
print(type(decimal))

division = 23 / 5

print(division)
print(type(division))

remainder = 23 % 5

print(remainder)
print(type(remainder))

divisor = 23 // 5

print(divisor)
print(type(divisor))


def fahrenheit_to_celsius(f):
    c = (f - 32) * (5 / 9)
    return "{:.3f}".format(c)


print(fahrenheit_to_celsius(451))
print(fahrenheit_to_celsius(451) == 232.778)
