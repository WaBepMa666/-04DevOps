# 6. Угадай число
import random

number = random.randint(1, 100)
attempts = 0

print("Угадай число (1-100)")
while True:
    guess = int(input("Ваше число: "))
    attempts += 1
    if guess < number:
        print("Больше")
    elif guess > number:
        print("Меньше")
    else:
        print(f"Правильно! Попыток: {attempts}")
        break
