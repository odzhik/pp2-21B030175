#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:

"""Hello! What is your name?
KBTU
Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12
Your guess is too low.
Take a guess.
16
Your guess is too low.
Take a guess.
19
Good job, KBTU! You guessed my number in 3 guesses!"""

import random
def guess(g, name, count):
    while count < 20:
        count += 1
        x = int(input('Take a guess'))
        if x != g:
            if x < g:
                print('Your guess is too low')
            elif x > g:
                print('Your guess is too high')
        else:
            print('Good job, '+ name +'! You guessed my number in '+ str(count) +'guesses')
            break

name = input('Hello! What is your name?')
print('Well, '+ name + ', I am thinking of a number between 1 and 20.')
g = random.randrange(1, 20)

guess(g, name, 0)