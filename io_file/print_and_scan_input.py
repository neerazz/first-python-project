print("Hello, This is Neeraj.")

bot_name = input("Enter the Name:")
birth_year = input("Enter birth Year:")
print(f"Hello! My bot_name is {bot_name}.")
print(f"I was created in {birth_year}.")
print(f"What a great owner you have, {bot_name}.")

print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
# age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
remainder3 = int(input())  # Cast the input to int
remainder5 = int(input())
remainder7 = int(input())
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")

print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
counter = int(input())

for i in range(0, counter+1):
    print(f"{i} !")

print('Completed, have a nice day!')
