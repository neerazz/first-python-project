import math
import random

print(math.pi)
print(math.e)
print(math.sqrt(2))
print(math.sin(math.pi / 2))


value = 4.35
print(math.ceil(value))
print(math.floor(value))
print(round(value) == math.floor(value))

value = 4.78
print(round(value) == math.ceil(value))


list = list(range(1, 25))
random.shuffle(list)
print(f"Shuffled list: {list}")
print(f"Random number form list: {random.choice(list)}")
print(f"Pick 5 non-dublicate random numbers from the list: {random.sample(list, 8)}")
print(f"Pick 5 random numbers from the list: {random.choices(list, k=8)}")

print(random.randint(1, 100))
