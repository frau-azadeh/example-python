import random

number = random.randint(1,10)
guess = None
tries = 0

print("please guess number between 1 and 10:")

while guess !=number:
    guess = int(input("Your geuss:"))
    tries += 1

    if guess<number:
        print("Guess a bigger number")
    elif guess>number:
        print("Guess a smaller number")

print(f"Well done! The number was {number}, and you guessed it in {tries} tries.")
