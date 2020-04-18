'''
Write a binary search function which searches an item in
a sorted list. The function should return the index of element
to be searched in the list.
'''

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(key):
    start = 0
    end = len(li) - 1

    mid = int((start + end) / 2)
    if li[mid] == key:
        return mid

    elif li[mid] < key:
        start = mid + 1

    else:
        end = mid - 1


key = int(input('Enter the element to be searched: '))
print(f'Index of {key} is: {binary_search(key)}')
