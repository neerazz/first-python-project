file_name = "print_and_scan_input.py"


def open_and_read_file(name):
    file = open(name)
    str = file.readlines()
    file.close()
    return str


def open_and_read_all_in_file(name):
    file = open(name)
    str = file.read()
    file.close()
    return str


print("*******************************")
print(open_and_read_file(file_name))
print("*******************************")
print(open_and_read_all_in_file(file_name))
