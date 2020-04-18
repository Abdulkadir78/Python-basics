'''
Write a program which takes 2 digits, X, Y as input and generates
a 2-dimensional array. The element value in the i-th row and j-th
column of the array should be i*j.
Example
Suppose the following inputs are given to the program:
3, 5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''


dimensions = input('Enter X,Y: ')
l = dimensions.split(',')
rows = int(l[0])
columns = int((l[1]))
l2 = []

for i in range(rows):
    l3 = []
    for j in range(columns):
        l3.append(i * j)
    l2.append(l3)

print(l2)
