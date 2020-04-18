'''
Write a program that computes the net amount of a bank account 
based a transaction log from console input. The transaction log 
format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''


net_amount = 0
print('D - Deposit\nW - Withdrawal\nC - Check balance\nE - Exit\n')

choice = input('\nEnter your choice: ')
choice = choice.upper()

while choice != 'E':
    if choice == 'D':
        deposit_amount = float(input('Enter the amount to be deposited: '))
        net_amount = net_amount + deposit_amount

    elif choice == 'W':
        if net_amount == 0:
            print('Not enough balance\n')
        else:
            withdrawal_amount = float(
                input('Enter the amount to be withdrawn: '))
            if withdrawal_amount > net_amount:
                print('Not enough balance\n')
            else:
                net_amount = net_amount - withdrawal_amount

    elif choice == 'C':
        print('Balance: ', net_amount)

    elif choice == 'E':
        break

    else:
        print('Invalid choice\n')

    choice = input('\nEnter your choice: ')
    choice = choice.upper()

print('Net amount: ', net_amount)
