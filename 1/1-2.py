import os, math

f = open("/home/igor/Programowanie/Python/advent-of-code-2019/1/1/input.txt", "r")
lines = f.readlines()

sum = 0

for line in lines:
    mass = line.rstrip()
    fuel = int(mass)
    while fuel > 0:
        fuel = math.floor(fuel / 3) - 2
        if(fuel >= 0 ):
            sum += fuel    
    
print(sum)