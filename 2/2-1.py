import os, math

f = open("/Users/igor/Programowanie/advent-of-code-2019/2/input.txt", "r")
lines = f.readlines()
opcodes = []
for op in lines[0].split(','):
    opcodes.append(int(op))
print(opcodes)
index = 0

while opcodes[index] != 99:
    current_opcode = opcodes[index]
    if opcodes[index] == 1:
        opcodes[opcodes[index+3]] = opcodes[opcodes[index+2]] + opcodes[opcodes[index+1]]
    elif opcodes[index] == 2:
        opcodes[opcodes[index+3]] = opcodes[opcodes[index+2]] * opcodes[opcodes[index+1]]
    index += 4

str_opcodes = []
for op in opcodes:
    str_opcodes.append(str(op))

print(",".join(str_opcodes))


