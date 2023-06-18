a = float(input("Please enter a number: "))
c = input("Please enter a calcualtion method: ")
b = float(input("Please enter a number: "))

if c == "+":
    result = a + b
    print(result)
elif c == "-":
    result = a - b
    print(result)
elif c == "*":
    result = a * b
    print(result)
elif c == "/":
    result = a / b
    print(result)
else:
    print("Calculation has failed")