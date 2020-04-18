'''
Given a sorted list with duplicates and a target number 'n',find
the range in which the number exists(represented as a
tuple(low, high),both inclusive.If the number does not exist in
the list, return (-1, -1))
Example:
Input: [1, 2, 3, 4, 5, 3, 6]
n = 3
Output: (2, 5)
'''

l = [1, 2, 3, 4, 5, 3, 6]


def find_num(l, n):
    if n not in l:
        return (-1, -1)

    else:
        start = l.index(n)   # index of first occurence of 'n'
        l[start] = '-'       # replacing that number with '-'
        end = l.index(n)     # index of second(actually first) occurence of 'n'
        return (start, end)


print(find_num(l, 3))


'''
ALTERNATE SOLUTION 1 :

l = [1, 2, 3, 4, 5, 3, 6]


def find_num(l, n):
    if n not in l:
        return (-1, -1)

    else:
        start = l.index(n)
        l.reverse()         
        temp_end = l.index(n) + 1
        end = len(l) - temp_end
        return (start, end)


print(find_num(l, 3))
'''

'''
ALTERNATE SOLUTION 2:

def find_num(l, n):
    index = []
    count = 0
    for number in l:
        if number == n:
            index.append(count)  # adding all the indexes of 'n'
        count += 1

    if len(index) == 0:
        return (-1, -1)
    else:
        return (index[0], index[-1])


print(find_num([1, 2, 1, 5, 3], 1))

'''
