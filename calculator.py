def add(a, b):
    return a+b
def subtrac(a, b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "error"
    return a/b
a = float(input("first number: "))
b = float (input("second number: "))
operator = input ("enter your operation (+, -, *, /): ")

if operator == "+":
    result = add (a,b)
elif operator == "-":
    result = subtrac (a,b)
elif operator == "*":
    result = multiply(a,b)
elif operator == "/":
    result = divide (a,b)
else:
    result = "operator is not valid"

print("Result:", result)
