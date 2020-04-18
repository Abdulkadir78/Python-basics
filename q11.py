'''
Write a program which accepts a sequence of comma separated
4 digit binary numbers as its input and then check whether they
are divisible by 5 or not. The numbers that are divisible by 5
are to be printed in a comma separated sequence.
Example:
0100, 0011, 1010, 1001
Then the output should be:
1010
'''


binary_numbers = input(
    'Enter a comma separated sequence of 4 digit binary numbers: ')

l = binary_numbers.split(',')
l2 = []
for binary in l:
    num = int(binary, 2)
    if num % 5 == 0:
        l2.append(binary)

print(', '.join(l2))
