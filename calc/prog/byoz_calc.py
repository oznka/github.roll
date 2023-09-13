def main(a, c, b):
    """
    a = float(input("Please enter a number: "))
    c = input("Please enter a calcualtion symbol(+, -, *, /): ")
    b = float(input("Please enter a number: "))
    """
    if c == "+":
        result = a + b
        return(result)
    elif c == "-":
        result = a - b
        return(result)
    elif c == "*":
        result = a * b
        return(result)
    elif c == "/":
        result = a / b
        return(result)
    else:
        return("Calculation has failed")



