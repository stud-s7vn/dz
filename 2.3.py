import random

correct_answer = random.randint(1, 10)
guesses = 3
for i in range(3):
    guess = int(input("guess the number from 1 to 10: "))
    if guess == correct_answer:
        print("correct!")
        break
    else:
        print("Wrong!")
