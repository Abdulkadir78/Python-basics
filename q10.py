'''
Write a program that accepts a sequence of whitespace separated 
words as input and prints the words after removing all duplicate 
words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''


words = input('Enter whitespace separated words: ')

l = words.split(' ')
s = set(l)
l2 = list(s)
l2.sort()
print(' '.join(l2))
