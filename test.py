# Write your string index below
# Start with 'Hello World'
# and make sure to match spaces and capitalization exactly
my_dict = {}

for i in range(0, 26):
    base = ord("a")
    cur = base + i
    cur_char = chr(cur)
    my_dict[cur_char] = i


# print(my_dict)


def lettersum(word):
    sum = 0
    for c in word:
        sum += my_dict[c] + 1 if c in my_dict else 0
    return sum


def myfunc(word):
    result = ""
    for idx, c in enumerate(word):
        if idx % 2 == 0:
            result += c.lower()
        else:
            result += c.upper()
    return result