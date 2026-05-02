#tad bit of ai used here
start = int(input("enter first number: "))
end = int(input("enter second number: "))


a = min(start, end)
b = max(start, end)

print(f"numbers between {a} and {b}:")

for i in range(a, b + 1):
    print(i, end=" ")