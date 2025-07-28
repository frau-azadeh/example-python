count = int(input("Enter your count number"))
numbers = []

for i in range(count):
    num = float(input(f"number {i+1}:"))
    numbers.append(num)

print("List number:", numbers)

max_number = max(numbers)
print("max is:", max_number)