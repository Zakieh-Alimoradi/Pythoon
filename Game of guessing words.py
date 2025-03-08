import random

def guess_number():
    number = random.randint(1, 100)
    guesses = 0

    while True:
        guess = int(input("what is your guess?"))
        guesses += 1

        if guess < number:
            print("number is bigger")
        elif guess > number:
            print("number is smaller")
        else:
            print(f"good job! your number is {number} and you guess after {guesses} times")
            break

guess_number()