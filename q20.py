'''
Define a class named Shape and its subclass Square. The Square
class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the
shape where Shape's area is 0 by default.

'''


class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return (f'Area: {0}')


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (f'Area: {self.length ** 2}')


length = int(input('Enter the length: '))
square = Square(length)
print(square.area())
