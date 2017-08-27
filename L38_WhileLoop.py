import random

highest = 10
number = random.randint(1, highest)
guess = int(input('Guess any number between 1 and {}: '.format(highest)))

while guess != number:
    if guess < 1 or guess > highest:
        guess = int(input("Sorry, that is not in the correct range. Please enter a number in the range: "))
    elif guess < number:
        guess = int(input('Guess higher: '))
    elif guess > number:
        guess = int(input('Guess lower: '))

print('Congratulations!!!, you have guessed the number! The number is {}.'.format(guess))
