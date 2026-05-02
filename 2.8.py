for i in range(100):
    a = int(input("first number: "))
    b = int(input("second number: "))
    diya = str(input("what action(+ - * /)? "))
    if b == 0 and diya == "/":
        print("you cannot divide with 0")
    elif diya == "+":
        result = (a + b)
        print(result)
    elif diya == "-":
        result = (a - b)
        print(result)
    elif diya == "*":
        result = (a * b)
        print(result)
    elif diya == "/":
        result = (a / b)
        print(result)
    else:
        print("you cant do that")
