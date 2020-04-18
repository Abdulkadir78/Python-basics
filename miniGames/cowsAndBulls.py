'''
Cows and bulls game
The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a
4-digit number. For every digit that the user guessed correctly
in the correct place, they have a 'bull'. For every digit the user
guessed correctly in the wrong place is a 'cow'.
4 bulls win the game
'''

import random

number = str(random.randint(1000, 9999))
trials = 0


def check_guess(number, guess):
    cows = 0
    bulls = 0

    if guess == number:
        bulls = 4

    else:
        for i in range(4):
            if guess[i] in number:
                if guess[i] == number[i]:
                    bulls += 1
                else:
                    cows += 1

    return cows, bulls


print("Type 'exit' anytime to stop\n")
while True:
    guess = input('> ').lower()

    if guess == 'exit':
        break

    elif len(guess) != 4:
        print('Please enter a 4 digit number\n')

    else:
        trials += 1
        cows, bulls = check_guess(number, guess)
        print(f'{cows} cows, {bulls} bulls')

        if bulls == 4:
            print(f'\nThe number was {number}')
            print(f'Number of trials: {trials}')
            break
