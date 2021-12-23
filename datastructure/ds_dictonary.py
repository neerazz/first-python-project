from collections import OrderedDict

from sortedcontainers import SortedDict

my_disc = dict()
my_ordered_disc = OrderedDict()
my_sorted_disc = SortedDict()


def insert(key, value):
    my_disc[key] = value
    my_ordered_disc.setdefault(key, value)
    my_sorted_disc.setdefault(key, value)


def get(key):
    return [my_disc[key], my_ordered_disc.get(key), my_sorted_disc.get(key)]


def get_first():
    return [None, my_ordered_disc.popitem(False), my_sorted_disc.peekitem(0)]


def remove(key):
    # pop(key) -> will remove the item and return the value from dict.
    #   But will through Exception when there is no any key.
    result = [my_disc.pop(key, None),
              my_ordered_disc.pop(key, None),
              my_sorted_disc.pop(key, None)]
    return result


def contains_key(key):
    result = [key in my_disc, key in my_ordered_disc, key in my_sorted_disc]
    return result


def print_all():
    print("********************* Start ***************************")
    print(my_disc)
    print(my_ordered_disc)
    print(my_sorted_disc)
    print("********************* End ***************************")


def print_other_properties():
    print("********************* Start ***************************")
    print(f"Length = {len(my_disc)}")
    print(f"Length = {len(my_ordered_disc)}")
    print(f"Length = {len(my_sorted_disc)}")
    print(f"Keys = {my_disc.keys()} and Values = {my_disc.values()}")
    print(f"Keys = {my_ordered_disc.keys()} and Values = {my_ordered_disc.values()}")
    print(f"Keys = {my_sorted_disc.keys()} and Values = {my_sorted_disc.values()}")
    print("********************* End ***************************")


print_all()
insert("batman", 10)
print_all()
insert("antman", 15)
print_all()
insert("ironman", 5)
print_all()
print_other_properties()
print(get("antman"))
print(contains_key("batman"))
print(remove("ironman"))
print_all()
print(remove("testman"))
print(get_first())
