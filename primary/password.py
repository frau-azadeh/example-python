import random

name = input("What is your name: ")
print(f"Your name is: {name}")

number = random.randint(100, 999)
password = name + str(number)

print(f"Your generated password is: {password}")
