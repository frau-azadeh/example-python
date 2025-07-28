numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}:"))
    numbers.append(num)

print ("All numbers:", numbers)

for n in numbers:
    if n % 2 == 0:
        print (n, "Is Even")
    else :
        print (n, "Is Odd")