grade = int(input("grade from 0 to 100: "))
if grade >= 0 and grade <= 49:
    print("insuficient grade")
elif grade >= 50 and grade <= 69:
    print("suficient grade")
elif grade >= 70 and grade <= 89:
    print("good grade")
elif grade >= 90 and grade <= 100:
    print("perfect grade")
