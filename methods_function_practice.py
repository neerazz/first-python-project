# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb
from math import sqrt


def lesser_of_two_evens(a, b):
    def is_even(n):
        return n % 2 == 0

    if is_even(a) and is_even(b):
        return min(a, b)
    else:
        return max(a, b)


def animal_crackers(word):
    split = word.split()
    return len(split) == 2 and split[0][0] == split[1][0]


def makes_twenty(n1, n2):
    return n1 == 20 or n2 == 20 or n1 + n2 == 20


def old_macdonald(name):
    chars = []
    for i, char in enumerate(name):
        if i == 0 or i == 3:
            chars.append(char.upper())
        else:
            chars.append(char)
    result = ""
    for char in chars:
        result += char
    return result


def master_yoda(text):
    return text[::-1]


def almost_there(n):
    return (90 <= n <= 110) or (190 <= n <= 210)


def has_33(nums):
    count_3 = 0
    for num in nums:
        count_3 = count_3 + 1 if num == 3 else 0
        if count_3 == 2: return True
    return False


def paper_doll(text):
    result = [c * 3 for c in text]
    return "".join(result)


def blackjack(a, b, c):
    three_sum = a + b + c
    if three_sum <= 21:
        return three_sum
    elif 11 in [a, b, c]:
        three_sum -= 10
    return three_sum if three_sum <= 21 else "BUST"


def summer_69(arr):
    ignore = False
    total = 0
    for num in arr:
        if ignore:
            if num == 9:
                ignore = False
        elif num == 6:
            ignore = True
        else:
            total += num
    return total


def spy_game(nums):
    zeros = 0
    for num in nums:
        if num == 0:
            zeros += 1
        elif num == 7:
            if zeros == 2:
                return True
    return False


def count_primes(num):
    count = 0
    not_prime = [False] * num
    for i in range(2, num):
        if not not_prime[i]:
            count += 1
            j = 2
            while j * i < num:
                not_prime[j * i] = num
                j += 1
    return count


def pattern():
    return {'a': [[2], [1, 3], [0, 1, 2, 3, 4], [0, 4], [0, 4]],
            'b': [[0, 1, 2, 3], [0, 4], [0, 1, 2, 3], [0, 4], [0, 1, 2, 3]],
            'c': [[0, 1, 2, 3, 4], [0], [0], [0], [0, 1, 2, 3, 4]],
            'd': [[0, 1, 2, 3], [0, 4], [0, 4], [0, 4], [0, 1, 2, 3]],
            'e': [[0, 1, 2, 3, 4], [0], [0, 1, 2, 3, 4], [0], [0, 1, 2, 3, 4]]}


def print_big(letter):
    cur_pattern = pattern()[letter]
    grid = [[" "] * 5 for _ in range(5)]
    for i, row in enumerate(cur_pattern):
        for j in row:
            grid[i][j] = "*"
    result = ""
    for row in grid:
        result += "".join(row)
        result += "\n"
    return result


print(print_big('a'))
print(print_big('b'))
print(print_big('c'))
print(print_big('d'))
print(print_big('e'))
