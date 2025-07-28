grades = []
count = int(input("Enter your number"))
for i in range(count):
    grade = float(input(f"grade {i+1}:"))
    grades.append(grade)


avarage = sum(grades)/len(grades)
print(f"your avarage is:", avarage)

if avarage>=12:
    print("accept")
else:
    print("regect")
