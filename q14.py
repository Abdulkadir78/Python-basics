'''
Write a program that accepts a sentence and calculate the number 
of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

'''


sentence = input('Enter a string: ')
upper = 0
lower = 0

for i in sentence:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print('Upper case: ', upper)
print('Lower case: ', lower)
