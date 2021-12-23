def direct():
    print("This is the direct function in one.py file.")


def in_directly():
    print("This is the in_directly function in one.py file.")


def func():
    print("This is a function in one.py")


print("Top level print in one.py")

if __name__ == '__main__':
    print("one.py is run directly.")
    direct()
else:
    print("one.py is been imported.")
    in_directly()
