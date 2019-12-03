import os, math

f = open("/home/igor/Programowanie/Python/advent-of-code-2019/1/1/input.txt", "r")
lines = f.readlines()


sum = 0

for line in lines:
    mass = line.rstrip()
    mass = int(mass)
    fuel = math.floor(mass / 3) - 2
    sum += fuel
    
print(sum)