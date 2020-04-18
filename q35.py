'''
Please write a program which counts and prints the numbers of
each character in a string input by console.

Example:
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a, 2
b, 2
c, 2
d, 1
e, 1
f, 1
g, 1
'''

string = input('Enter a string: ')
l = []
for character in string:
    if character not in l:
        l.append(character)
        print(f'{character}, {string.count(character)}')


'''
ALTERNATE SOLUTION:

dic = {}
string = input('Enter a string: ')

for character in string:
    dic[character] = dic.get(character, 0) + 1

print('\n'.join(['%s, %s' % (k, v) for k, v in dic.items()]))
'''
