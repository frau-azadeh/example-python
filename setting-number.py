import sys
num = int (input("Enter your number:"))

while True:
    print("\nChoose an option:")
    print("1) Square the number")
    print("2) Check even or odd")
    print("3) Exit")

    choice = input("Your choice (1/2/3): ")

    if choice == "1":
        print("Result:", num ** 2)
    elif choice == "2":
        if num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    elif choice == "3":
        print ("Goodbye")
        break
    else:
        print("Invalid choice. please try again")