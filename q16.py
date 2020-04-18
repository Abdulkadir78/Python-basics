'''
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1, 2, 3, 4, 5, 6, 7, 8, 9
Then, the output should be:
1, 9, 25, 49, 81

'''
numbers = input('Enter comma separated sequence of numbers: ')
temp_list = numbers.split(',')
l = []
final_list = []  # this list is used just for converting the integer list 'l' to a comma separated string

for number in temp_list:
    if int(number) % 2 != 0:
        l.append(int(number) ** 2)

for number in l:
    # converting integer list 'l' to a string list
    final_list.append(str(number))

print(', '.join(final_list))
