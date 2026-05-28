#5/28/2026
import random 

print ("Welcome to the Number Guessing Game!")

max_number = int(input("Enter the maximum number for the range: "))


secrete_number = random.randint(1, max_number)

attempts = 0

guess = None


while guess != secrete_number:
    guess = int(input(f"Guess a number between 1 and {max_number}: "))

    attempts = attempts + 1

    if guess < secrete_number:
        print("Guess too Low! Try again.")

    elif guess > secrete_number:
        print("Guess too High! Try again")

    else:
        print(f"Congradulations! You guessed it in {attempts} attempts!")

print(f"The secrete number was {secrete_number}. Thanks for playing!")
