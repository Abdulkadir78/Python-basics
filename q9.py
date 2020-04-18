'''
Write a program that accepts sequence of lines as input and 
prints the lines after making all characters in the sentence 
capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

'''


l = []
print('Press ENTER to stop')
while True:
    statement = input()
    if statement:
        l.append(statement.upper())

    else:
        break

for statement in l:
    print(statement)
