import random
import string

print("Welcome to Random Password Generator!!")

#fetching all letters,digits,symbols using string module
letter = string.ascii_letters
symbol = string.punctuation
digit = string.digits

all = letter + symbol + digit
#generating password using random module
pass_length = int(input("Enter the length of password between 8 and 72: "))
if (pass_length >= 8 and pass_length <= 72):
    temp = random.sample(all, pass_length)
    password = "".join(temp)
    print(f"Your desired password is \"{password}\"")
else:
    print("Invalid Input!\nPlease! Enter the length of password between 8 and 72.")