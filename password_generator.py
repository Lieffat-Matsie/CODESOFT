import random

# this is to set password to have mixture of symbols, numbers, big letters & small letters
big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letters = big_letters.lower()
numbers_ = 1234567890
symbols = "()!@#$%^&*_+-\/?.,="

# set everything to true to makes sure password has a mixture of all letters,symbols, numbers & letters
upper, lower, nums, syms = True, True, True, True

# set an empty string
all = ""

# if big letters are set to true, include them in the password
if upper:
    all += big_letters
# if small case letters are set to true, include them in the password
if lower:
    all += small_letters
if nums:
# if numbers are set to true, include them on the password  
    all += str(numbers_)
# if symbols are set to true, include them on the password  
if syms:
    all += symbols

# how long the password should be
length_of_password = 12
# how many passwords to generate
amount_of_passwords = 3

# loop password to print how long the password should be and how many times to print
for x in range(amount_of_passwords):
    password = "".join(random.sample(all, length_of_password))
# finally print the password  
    print(password)
