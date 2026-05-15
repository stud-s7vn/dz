

result = []

def divider(a, b):
    if a < b:
        raise ValueError("a must be greater than or equal to b")
    if b > 100:
        raise IndexError("b cannot be greater than 100")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, (1, 2): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Skipping key '{key}' due to error: {e}")

print("\nFinal results:")
print(result)