'''
Write a Python program to add the digits of a positive
integer repeatedly until the result has a single digit.
Example:
Input: 59
Output: 5
Step 1: 5 + 9 = 14
Step 2: 1 + 4 = 5
'''

number = int(input('Enter a number: '))

if number > 0:
    result = number
    while result > 9:
        remainder = result % 10
        number = int(result / 10)
        result = number + remainder

    print(result)

else:
    print('Enter a positive integer')

'''
ALTERNATE SOLUTION:

number = int(input('Enter a number: '))
if number > 0:
    result = (number - 1) % 9 + 1
    print(result)

else:
    print('Enter a positive integer')
'''
