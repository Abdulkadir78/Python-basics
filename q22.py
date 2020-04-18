'''
A robot moves in a plane starting from the original point(0, 0).
The robot can move toward UP, DOWN, LEFT and RIGHT with given
steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program 
to compute the distance from current position after a sequence of 
movement and original point. If the distance is a float, then 
print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

'''
import math

print('\nUP\nDOWN\nLEFT\nRIGHT\nEXIT\n')

direction = input('Enter the direction: ').upper()
hsteps = 0
vsteps = 0

while True:
    if direction == 'UP':
        steps = int(input('Enter the number of steps: '))
        vsteps += steps

    elif direction == 'DOWN':
        steps = int(input('Enter the number of steps: '))
        vsteps -= steps

    elif direction == 'LEFT':
        steps = int(input('Enter the number of steps: '))
        hsteps -= steps

    elif direction == 'RIGHT':
        steps = int(input('Enter the number of steps: '))
        hsteps += steps

    elif direction == 'EXIT':
        break

    else:
        print('Invalid direction\n')

    direction = input('\nEnter the direction: ').upper()

distance = int(math.sqrt(vsteps ** 2 + hsteps ** 2))
print(f'\nTotal distance: {distance}')


'''
# ALTERNATE SOLUTION: 

pos = [0, 0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass

print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))
'''
