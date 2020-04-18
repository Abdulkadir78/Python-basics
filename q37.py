'''
Write a program which accepts a string from console and print the 
characters that have even indexes.
Example:
If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld
'''

string = input('Enter a string: ')
l = []

for character in string:
    if string.index(character) % 2 == 0:
        l.append(character)

print(''.join(l))

'''
ALTERNATE SOLUTION:

s = input('Enter a string: ')
print(s[::2])
'''
