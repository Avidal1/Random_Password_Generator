import random
import string

# password generator no loop - I'll keep this one commented out but you do as you wish

# list_letters = string.ascii_lowercase + string.ascii_uppercase
# list_numbers = string.digits
# list_symbols = string.punctuation
#
# ask_letters = int(input("How many letters would you like (limit 9 letters) ? \n >> "))
# ask_numbers = int(input("How many numbers would you like (limit 9 digits) ? \n >> "))
# ask_symbols = int(input("How many symbols would you like (limit 9 characters) ? \n >> "))
#
# the_letters = random.choices(list_letters, k=ask_letters)
# the_numbers = random.choices(list_numbers, k=ask_numbers)
# the_symbols = random.choices(list_symbols, k=ask_symbols)
# together = the_letters + the_numbers + the_symbols
#
# if (ask_letters < 10) and (ask_numbers < 10) and (ask_letters < 10):
#     random.shuffle(together)
#     together_without_characters = "".join(together)
#     print(f"hard level complete: {together_without_characters}")
# else:
#     print(f"You didn't follow directions, you picked {ask_letters} Letters, {ask_numbers} Numbers, {ask_symbols} Symbols")


# with a for loop

ask_letters = int(input("How many letters you want? \n >> "))
ask_numbers = int(input("How many numbers you want? \n >> "))
ask_symbols = int(input("How many symbols you want? \n >> "))

letters = string.ascii_lowercase + string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

password = []
for char in range(1, ask_letters + 1):
    password += random.choice(letters)


for char in range(1, ask_numbers + 1):
    password += random.choice(numbers)


for char in range(1, ask_symbols + 1):
    password += random.choice(symbols)

print(password)
random.shuffle(password)

print(password)

password_string = ''
for char in password:
    password_string += char

print(password_string)
