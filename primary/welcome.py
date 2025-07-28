name = input("What is your name? ")
age = int(input("How old are you? "))

if age >= 18:
    print("Your account is full,", name, "- Welcome!")
else:
    print("Your account is disabled,", name, "- Unfortunately.")
