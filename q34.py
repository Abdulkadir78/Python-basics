'''
Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.
'''


class numbers():
    def gen(self, n):
        for number in range(n):
            if number % 7 == 0:
                yield number


my_generator = numbers()

n = int(input('Enter n: '))

for result in my_generator.gen(n):
    print(result)
