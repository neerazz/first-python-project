my_set = set()


def add(val):
    print(f"Adding {val} in set.")
    my_set.add(val)


def contains(val):
    return val in my_set


def remove(val):
    print(f"Removing {val} in set.")
    my_set.remove(val)


def print_all():
    print(f"Set Size : {len(my_set)}.")
    print(f"Elements in set: {my_set}")


add(10)
add(20)
print_all()
add(10)
print_all()
print(contains(10))
remove(10)
print_all()
