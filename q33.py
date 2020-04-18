'''
With a given list[12, 24, 35, 24, 88, 120, 155, 88, 120, 155],
write a program to print this list after removing all duplicate
values with original order reserved.
'''


l = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
l2 = []
l3 = []

for number in l:
    if number not in l2:
        l2.append(number)
        l3.append(number)

print(l3)
