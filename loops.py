def for_loop_string(string):
    print(f"{'*' * 5} For Loop for String: {string} {'*' * 5} ")
    for c in string:
        print(c)


def for_loop_string_adv(string):
    print(f"{'*' * 5} For Loop for String: {string}, with advanced stuff {'*' * 5}")
    for c in string:
        if c[0] == 'T':
            print(c)


def for_loop_list(lst):
    print(f"{'*' * 5} For Loop for list: {lst} {'*' * 5} ")
    for num in lst:
        if num.lower() == "Start".lower() or num.lower() == "END".lower():
            continue
        if num.lower() == "END".lower():
            break
        else:
            print(num)


def for_loop_list_adv(lst):
    print(f"{'*' * 5} For Loop for list : {lst}, with Advanced Stuff: {'*' * 5} ")
    for i in range(0, len(lst), 2):
        print(f"Value at index : {i} is: {lst[i]}")

    for i, num in enumerate(lst):
        print(f"Value at index : {i} is: {num}")

    for i, (a, b) in enumerate(lst):
        print(f"Value at index : {i} is: a: {a} & b: {b}")


def for_loop_dic(dic):
    print(f" {'*' * 5} For Loop for Dictionary: {dic} {'*' * 5} ")
    for key in dic:
        print(f"Key : {key}")

    for key, value in dic.items():
        print(f"Key : {key} and value : {value}")

    for value in dic.values():
        print(f"Value : {value}")


def while_loop_string(string):
    print(f"{'*' * 5} While Loop for String: {string} {'*' * 5} ")
    i = 0
    str_len = len(string)
    while i < str_len:
        print(string[i])
        i += 1


while_loop_string("This is a string")
for_loop_string("This is a string")
for_loop_list(["Start", "This", "is", "a", "list", "end"])
for_loop_list_adv([(1, 2), (3, 4), (4, 5), (6, 7)])
for_loop_dic({"k1": 1, "k2": 2})
