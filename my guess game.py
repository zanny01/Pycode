# This is a guess the number game.

import random
print('Hello, what is your name?')
name = input ()
secretNumber = random.randint(1,20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times.
for guessesTaken in range (1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')

    elif guess > secretNumber:
        print('your guess is too high.')

    else:
        break# This condition is the correct guess!

    if guess == secretNumber:
        print('Good job, ' + name+'! you guessed my number incorrectly')

    else:
              print('Nope. The number I was thinking of was ' + str(secretNumber ))

                    
