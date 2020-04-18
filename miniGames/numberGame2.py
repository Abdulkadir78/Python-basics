'''
The user, will have in their head a number between 0 and 100.
The program will guess a number, and the user, will say whether it
is too high, too low, or the correct number.

'''

import random

start = 1
end = 100
l = list(range(start, end + 1))
trials = 0

number = input('Think of a number between 1 and 100\nPress ENTER when done  ')
print("\nType 'exit' anytime to stop\n")

guess = random.choice(l)   # selecting random number from the list
while True:
    print(f'\nIs it {guess}?\n')
    print('Go higher?(Press h)')
    print('Go lower?(Press l)')
    print('Correct?(Press c)\n')
    option = input('> ').lower()

    if option == 'exit':
        break

    elif option == 'c':
        trials += 1
        print(f'Number of trials: {trials}')
        break

    elif option == 'h':
        if guess == 100:
            print('\n\tCannot go any higher\n')
            continue
        start = guess + 1   # To reduce the search range
        if start <= end:
            trials += 1
            # selecting a random number from the new reduced range
            guess = random.randint(start, end)
        else:
            # If start becomes greater than end, then the user must
            # have done a mistake while choosing the hints
            print('\n\tI have already checked that range\n')
            break

    elif option == 'l':
        if guess == 1:
            print('\n\tCannot go any lower\n')
            continue
        end = guess - 1   # To reduce the search range
        if start <= end:
            trials += 1
            # selecting a random number from the new reduced range
            guess = random.randint(start, end)
        else:
            print('\n\tI have already checked that range\n')
            break

    else:
        print('Invalid option\n')


'''
ALTERNATE SOLUTION: Using binary search

l = [number for number in range(1, 101)]
start = 1
end = 100
trials = 0

number = input('Think of a number between 1 and 100\nPress ENTER when done  ')
print("\nType 'exit' anytime to stop\n")

while True:
    mid = (start + end) / 2
    guess = l[int(mid)]

    print(f'\nIs it {guess}?\n')
    print('Go higher?(Press h)')
    print('Go lower?(Press l)')
    print('Correct?(Press c)\n')
    option = input('> ').lower()

    if option == 'exit':
        break

    elif option == 'c':
        trials += 1
        print(f'Number of trials: {trials}')
        break

    elif option == 'h':
        if start <= end:
            trials += 1
            start = mid + 1
        else:
            print('\nI have already checked that range\n')
            break

    elif option == 'l':
        if start <= end:
            trials += 1
            end = mid - 1
        else:
            print('\nI have already checked that range\n')
            break

    else:
        print('Invalid option\n')
        
'''
