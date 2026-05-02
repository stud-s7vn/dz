name = str(input("what is you name? "))
age = str(input("how old are you? "))
print("Hi " + name + ", you are " + age + " years old.")

acces = False

if int(age) <= 18:
    print("access denied")
else:
    print("access granted")
    acces = True