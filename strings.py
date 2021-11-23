my_string = "Neeraj Is Working Hard"
print(my_string)

print("# ------------CommonFunctions----------------")
print(len(my_string))  # Length
print(my_string.find("Is"))
print(my_string.find("is", 10))
print(my_string.index("Is"))  # Throws Exception when char not found.

print("# --------Slicing------------------")
print(my_string[1])  # Second char
print(my_string[-1])  # Last char
print(my_string[1:])  # Everything from 1'st char
print(my_string[:4])  # From start till 3.Doesn't include 4.
print(my_string[1:3])  # From1to3-Excluding3.

print("# -------- Skip Slicing------------------")
print(my_string[::2])  # Start from beginning till the end, by skipping 2 chars.
print(my_string[::3])  # Start from beginning till the end, by skipping 3 chars.

print("# -------- Reverse Slicing------------------")
print(my_string[::-1])  # Reverse the string
print(my_string[17:0:-2])  # 0 to 17 chars by skipping 2 chars and reversing

print("# ------------- Other common functions ----------")
print(my_string.upper())  # Uppercase
print(my_string.lower())  # Lowercase
print(my_string.title())  # Titlecase/Camel Case
print("123".isdigit())  # Check if isdigit Will give true

print("# --------Split-----------")
print(my_string.split())  # Default splits on space. Returns list
print(my_string.split("i"))  # Splits on"i". Returns list

print("# ---------Formatting-------------")
print("# --------- # 1. String formatting -------------")
'''
1.String format method:
    All of these will produce: The quick brown fox.
'''
print("The {} {} {}".format("quick", "brown", "fox"))  # Interpolation inorder.
print("The {0} {1} {2}".format("quick", "brown", "fox"))  # Interpolation based on indexes
print("The {1} {0} {2}".format("brown", "quick", "fox"))  # Interpolation based on indexes
print("The {q} {b} {f}".format(b="brown", q="quick", f="fox"))  # Interpolation based on variables.

print("# --------- # 2.Floating point formatting -------------")
result = 100 / 7
print(result)  # 14.285714285714286
print("{:1.2f}".format(result))  # 14.29
print("{r:1.2f}".format(r=result))  # r=>rval,1=>Width(Space),2f=>two chars after decimal

print("# ----------f-Strings----------------")
name = "Jose"
age = 10
print(f"My name is {name} and my age is : {age}")  # "My name is Jose and my age is 10"
