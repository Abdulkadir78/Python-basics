'''
Write a function to compute 5/0 and use try/except to catch the
exceptions.

'''


def compute():
    result = 5 / 0
    return result


try:
    print(compute())

except ZeroDivisionError:
    print('Cannot divide by zero')
