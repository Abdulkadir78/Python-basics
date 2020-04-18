# Two player rock, paper, scissors game


from os import system, name


def clear():  # This function is used just to clear the screen through the script
              # It has no relation with the problem statement

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def check_winner(player1, player2):
    if player1 == player2:
        clear()  # clearing the screen using the function defined above
        print('\n\tIt is a tie!\n')

    elif player1 == 'r':
        clear()
        if player2 == 's':
            print('\n\tPlayer1 wins!\n')
        else:
            print('\n\tPlayer2 wins!\n')

    elif player1 == 'p':
        clear()
        if player2 == 'r':
            print('\n\tPlayer1 wins!\n')
        else:
            print('\n\tPlayer2 wins!\n')

    elif player1 == 's':
        clear()
        if player2 == 'p':
            print('\n\tPlayer1 wins!\n')
        else:
            print('\n\tPlayer2 wins!\n')


try:
    print('1 - Play\n2 - Exit\n')
    choice = int(input('Enter your option: '))
    clear()

    while choice != 2:
        if choice == 1:
            print('r - Rock\np - Paper\ns - Scissors\n')

            l = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

            print('Player 1:')
            player1 = input('Enter your choice: ').lower()
            if player1 not in l.keys():
                clear()
                print('Invalid choice\n')
                print('Game restarted\n')
                continue

            clear()  # clear the screen

            print('Player 2:')
            player2 = input('Enter your choice: ').lower()
            if player2 not in l.keys():
                clear()
                print('Invalid choice')
                print('Game restarted\n')
                continue

            check_winner(player1, player2)  # function to check the winner

            print(
                f'Player1 chose: {l[player1]}\nPlayer2 chose: {l[player2]}\n')

        elif choice == 2:
            break

        else:
            clear()
            print('Invalid choice\n')

        print('\n1 - Play\n2 - Exit\n')
        choice = int(input('Enter your option: '))
        clear()

except ValueError:
    print('Invalid choice!')
