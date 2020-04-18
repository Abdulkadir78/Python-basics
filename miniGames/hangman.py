# Hangman game

import random
from os import system, name


def clear():  # This function is used just to clear the screen through the script
              # It has no relation with the problem statement

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def random_word():  # To generate a random word
    with open('sowpods.txt', 'r') as words_file:
        word_list = words_file.readlines()

    # selecting a random word from the list of words
    word = list(random.choice(word_list))
    word.pop()  # To remove the '\n' from the word
    return word


def draw(wrong_guess):
    if wrong_guess == 1:
        print('      ____________')
        print('     |   /        |')
        print('     |  /         |')
        print("     | /          O")
        print('     |/')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('_____|______')

    elif wrong_guess == 2:
        print('      ____________')
        print('     |   /        |')
        print('     |  /         |')
        print("     | /          O")
        print('     |/           |')
        print('     |            |')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('_____|______')

    elif wrong_guess == 3:
        print('      ____________')
        print('     |   /        |')
        print('     |  /         |')
        print("     | /          O")
        print('     |/          /|')
        print('     |          / |')
        print('     |            |')
        print('     |')
        print('     | ')
        print('     |')
        print('_____|______')

    elif wrong_guess == 4:
        print('      ____________')
        print('     |   /        |')
        print('     |  /         |')
        print("     | /          O")
        print('     |/          /|\ ')
        print('     |          / | \ ')
        print('     |            |')
        print('     |')
        print('     |')
        print('     |')
        print('_____|______')

    elif wrong_guess == 5:
        print('      ____________')
        print('     |   /        |')
        print('     |  /         |')
        print("     | /          O")
        print('     |/          /|\ ')
        print('     |          / | \ ')
        print('     |            |')
        print('     |           /')
        print('     |          / ')
        print('     |')
        print('_____|______')

    elif wrong_guess == 6:
        print('      ____________')
        print('     |   /        |')
        print('     |  /         |')
        print("     | /          O")
        print('     |/          /|\ ')
        print('     |          / | \ ')
        print('     |            |')
        print('     |           / \ ')
        print('     |          /   \ ')
        print('     |')
        print('_____|______')


word = random_word()
final_word = ''.join(word)  # copy of the word to check the winning condition

guessed = ['_' for i in range(len(word))]  # For representing guessed letters
checked_words = []  # To keep track of already guessed letters

print("Type 'exit' anytime to stop\n")
print(f'The words has {len(word)} letters\n')
print(' '.join(guessed))

trials = 0
wrong_guess = 0  # only 6 wrong guesses are allowed

while wrong_guess < 6:
    letter = input('\nEnter a letter: ').upper()
    clear()  # To clear the screen

    if letter == 'EXIT':
        break

    elif letter in checked_words:
        print('Already guessed!\n')
        draw(wrong_guess)
        print(f'Wrong guesses left: {6 - wrong_guess}\n')
        print(' '.join(guessed))

    elif letter not in word:
        print('Incorrect!\n')
        checked_words.append(letter)
        wrong_guess += 1
        trials += 1
        draw(wrong_guess)
        print(f'Wrong guesses left: {6 - wrong_guess}\n')
        print(' '.join(guessed))

    else:
        checked_words.append(letter)
        while letter in word:
            index = word.index(letter)
            guessed[index] = letter
            # replacing the letter in the word with '_' (copy of word is kept for this reason)
            word[index] = '_'
        trials += 1
        draw(wrong_guess)
        print(f'Wrong guesses left: {6 - wrong_guess}\n')
        print(' '.join(guessed))

        if ''.join(guessed) == final_word:
            print('\n\tYou won!\n')
            print(f'Number of trials: {trials}')
            print(f'Wrong guesses: {wrong_guess}')
            break
else:
    print('\n\tGame over!')
    print(f"\nThe word was '{final_word}'")
