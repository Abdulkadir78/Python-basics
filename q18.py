'''
Write a program to compute the frequency of the words from the 
input. The output should output after sorting the key 
alphanumerically.
Suppose the following input is supplied to the program:
Input: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2: 2
3.: 1
3?: 1
New: 1
Python: 5
Read: 1
and: 1
between: 1
choosing: 1
or: 2
to: 1
'''

statement = input('Enter a string: ')
l = statement.split(' ')
l2 = []
for word in l:
    l2.append(f'{word}: {l.count(word)}')

s = set(l2)  # to remove duplicates
l2 = list(s)

l2.sort()

for result in l2:
    print(result)
