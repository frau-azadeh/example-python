numbers = []
for i in range (3):
    num = int(input(f"Enter number {i+1}:"))
    numbers.append(num)
print ("All numbers:", numbers)

for i in range(len(numbers)):
    print(f"Grade is : {numbers[i]}")

