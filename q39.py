'''
Write a program to guess a number that is randomly selected
between 1 and 100
'''

import random
random_number = random.randint(1, 100)

guess = int(input('\nEnter a number: '))
if guess == random_number:
    print('Correct answer!\n')

else:
    print(f'Wrong answer, the number was {random_number}')
