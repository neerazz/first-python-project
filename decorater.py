# This is a decorator function that will decorate a function:
#       1. Which prints stars at the beginning and at the end of the function.
def include_seperator(function):
    def wrapper():
        print_stars()
        print_function_name(function)
        function()
        print_stars()

    return wrapper


# This is a decorator function that will decorate a function:
#       1. Which prints stars at the beginning and at the end of the function.
#       2. The function can have different arguments
def include_seperator_2(function):
    def wrapper(*args, **kwargs):
        print_stars()
        print_function_name(function)
        function(*args, **kwargs)
        print_stars()

    return wrapper


# This is a decorator function that will decorate a function:
#       1. Which prints stars at the beginning and at the end of the function.
#       2. The function can have different arguments
#       2. The function can also return some value.
def include_seperator_3(function):
    def wrapper(*args, **kwargs):
        print_stars()
        print_function_name(function)
        func_result = function(*args, **kwargs)
        print_stars()
        return func_result

    return wrapper


def print_function_name(function):
    split = str(function).split()
    name = split[1] if len(split) > 1 else ""
    print(f"{' ' * 10} {name.replace('_', ' ').upper()} {' ' * 10}")


def print_stars():
    print(f"\n {'*' * 100}\n")
