'''
Write a program to find missing numbers from a list.
Example:
Input : [1, 2, 3, 4, 6, 7, 10]
Output: [5, 8, 9]
'''

l = [22, 23, 25, 29, 35]
l2 = []
start = l[0]
end = l[-1]

for number in range(start, end + 1):
    if number not in l:
        l2.append(number)

print(l2)
