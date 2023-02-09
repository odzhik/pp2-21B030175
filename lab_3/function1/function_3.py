#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

#12 * 4 + 23 * 2 = 94

def solve(numheads, numlegs):
    ns='No solutions!'
    for i in range(numheads + 1):
        j=numheads-i
        if 2*i + 4*j == numlegs:
            return i,j
        return ns,ns
    
numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))