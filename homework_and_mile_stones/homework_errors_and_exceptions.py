def problem1(input_list):
    print("Running Problem1: Handle exception thrown by the code")
    for i in input_list:
        try:
            pow_of_num = i ** 2
        except TypeError:
            print(f"List contains non-numeric element : {i}")
        else:
            print(pow_of_num)


def problem2(num1, num2):
    print("Running Problem2: Handle exception thrown by dividing to zero.")
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print(f"Invalid operation. Divisor is : {num2}, must not be zero.")
    else:
        print(f"Result of dividing {num1} with {num2} is {result}")
        return result
    finally:
        print("All Done!!")


if __name__ is not '__main__':
    print("Importing homework_errors_and_exceptions.py script")
