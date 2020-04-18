'''
Define a function that can accept two strings as input and print
the string with maximum length in console. If two strings have
the same length, then the function should print all strings line
 by line.

'''


def calculate_length(string_1, string_2):

    length_1 = len(string_1)
    length_2 = len(string_2)

    if length_1 > length_2:
        print(string_1)

    elif length_2 > length_1:
        print(string_2)

    else:
        print(f'{string_1}: {length_1}')
        print(f'{string_2}: {length_2}')


str_1 = input('Enter the first string: ')
str_2 = input('Enter the second string: ')

calculate_length(str_1, str_2)
