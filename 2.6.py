n = int(input("enter number n: "))

factorial = 1


if n < 0:
    print("factorial doesnt exist for negative numbers")
elif n == 0:
    print("factorial of number 0 equals 1")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"factorial of {n} (!{n}) equals: {factorial}")