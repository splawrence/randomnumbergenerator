from random import *
guess_count = 0
rand = int(randint(1, 100))
print("I've thought of a number from 1 through 100.")

while True:
    try:
        guess = int(input("Guess the number: "))
        break
    except ValueError:
        print("That is not a number.")
        continue

while True:
    if guess == rand:
        guess_count += 1
        break
    elif guess > 100:
        print("Number must be from 1 through 100.")
        while True:
            try:
                guess = int(input("Guess the number: "))
                break
            except ValueError:
                print("That is not a number.")
                continue
        guess_count += 1
        continue
    elif guess > rand:
        print("Too high.")
        while True:
            try:
                guess = int(input("Guess the number: "))
                break
            except ValueError:
                print("That is not a number.")
                continue
        guess_count += 1
        continue
    elif guess < rand:
        print("Too low. ")
        while True:
            try:
                guess = int(input("Guess the number: "))
                break
            except ValueError:
                print("That is not a number.")
                continue
        guess_count += 1
        continue
    else:
        guess = int(input("That is not a number. Try again: "))
        continue

print('Correct. You took %s guesses' % (guess_count))

