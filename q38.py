'''
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits
in a farm. How many rabbits and how many chickens do we have?
'''

total_heads = 35
total_legs = 94

for chickens in range(total_heads + 1):
    rabbits = total_heads - chickens

    # since chickens have 2 legs and rabbits have 4 legs
    if (2 * chickens + 4 * rabbits == total_legs):
        print(f'Chickens: {chickens}\nRabbits: {rabbits}')
