'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right.
1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when
the game ends, print this out.

'''


import random

number = random.randint(1, 9)
trials = 0


print("Type 'exit' anytime to stop")
try:
    while True:
        guess = input('\nEnter a number: ').lower()

        if guess == 'exit':
            break

        else:
            guess = int(guess)
            if guess < 0 or guess > 9:
                print('Enter numbers between 1 and 9 only\n')

            else:
                trials += 1
                if guess == number:
                    print('\nYou guessed the number correctly')
                    print(f'Number of trials: {trials}')

                    # start of a new game
                    number = random.randint(1, 9)
                    trials = 0
                    print('---------------------------')
                    print('\n\tNew game started\n')
                    print("Type 'exit' to stop\n")

                elif guess > number:
                    print('Go Lower\n')

                else:
                    print('Go higher\n')

except ValueError:
    print('Invalid entry\n')
