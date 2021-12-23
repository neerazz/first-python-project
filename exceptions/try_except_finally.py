from random import randint


def add(n1, n2):
    result = None
    try:
        result = int(n1) + int(n2)
    except ValueError:
        # Here you can handle the error, related to incorrect format.
        print(f"There is an error in the input values :{n1} & {n2}. Make sure you enter integers only.")
    except:
        # Here you can handle the error, other than the above two type
        print("Unexpected Error occurred.")
        print("Add went well. Result is : " + result)
    else:
        # Else, execute if no exception
        print("Add was successful.")
    finally:
        # Finally, block always gets executed either exception is generated or not
        print("I will run every time.")
        return result


def ask_for_input():
    user_input = None
    while True:
        try:
            user_input = int(input("Enter your input:"))
        except ValueError:
            print("Whoops!! That is not a number.")
            continue
        else:
            print(f"Finally got a valid user Input: {user_input}")
            break
        finally:
            print("I am going to ask you again! \n")
    return user_input


def input_for_add():
    system_input = randint(0, 2000)
    user_input = ask_for_input()
    input_sum = add(system_input, user_input)
    print(f"The input sum of {system_input} and {user_input} is {input_sum}")


input_for_add()
