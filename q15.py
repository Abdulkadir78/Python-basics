'''
Write a program that computes the value of a+aa+aaa+aaaa with a
given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

'''
a = input('Enter the value of a: ')
l = []
l.append(a)
result = int(a)
for i in range(3):
    l.append(a)
    result = result + int(''.join(l))

print(result)


'''
ALTERNATE SOLUTION 1:

a = input('Enter the value of a: ')
l = []
l.append(a)     # units place entered in the list

l.append(a)
tens = ''.join(l)

l.append(a)
hundreds = ''.join(l)

l.append(a)
thousands = ''.join(l)

result = int(a) + int(tens) + int(hundreds) + int(thousands)
print(result)
'''

'''
ALTERNATE SOLUTION 2:

a = input('Enter the value of a: ')
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
n4 = int("%s%s%s%s" % (a, a, a, a))
print (n1+n2+n3+n4)
'''
