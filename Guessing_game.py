import random
number = random.randint(1,100)
attempt = 0

print("Wanna play a Guessing game?\nGive it a chance!!\nLet's see in How many attempts will you guess the number correctly :)")

def guess_the_number():
    #for count total number of function calls
    global attempt
    attempt += 1
    #taking input and checking the guess
    guess = int(input("Enter your guessed number between 1 and 100: "))
    if(guess <= 0 or guess >= 100):
        print("Invalid input found!! Please enter number between 1 and 100 and Try again.")
        guess_the_number()
    elif (guess != number):
        print(f"Sorry :( you guessed it wrong, Try again.")
        if (guess > number):
            print("Your guess is greater than the number, Think Small :)")
        elif (guess < number):
            print("Your guess is lower than the number, Think Big :)")
        guess_the_number()
    else :
        print("Yeah!! you guessed it right :)")

guess_the_number()
print(f"Your total number of attempts is: {attempt}")