#Реалізувати генератор, який видає послідовність випадкових букв алфавіту.
import random
import time
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k','l','m','n','o','p',
    #theres definetly an easier way
    'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z'
]
for _ in range (10):
    bukva = random.randint(1, 26)
    print(alphabet[(bukva)])
    time.sleep(0.5)
    #it is what it is
    #what if i made it colorful

