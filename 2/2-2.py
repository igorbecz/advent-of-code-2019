import os, copy

def runAndReturnOutput(opcodes):
    index = 0

    while opcodes[index] != 99:
        if opcodes[index] == 1:
           opcodes[opcodes[index+3]] = opcodes[opcodes[index+2]] + opcodes[opcodes[index+1]]
        elif opcodes[index] == 2:
            opcodes[opcodes[index+3]] = opcodes[opcodes[index+2]] * opcodes[opcodes[index+1]]
        index += 4
    return opcodes[0]

def run(opcodes):
    index = 0

    while opcodes[index] != 99:
        if opcodes[index] == 1:
           opcodes[opcodes[index+3]] = opcodes[opcodes[index+2]] + opcodes[opcodes[index+1]]
        elif opcodes[index] == 2:
            opcodes[opcodes[index+3]] = opcodes[opcodes[index+2]] * opcodes[opcodes[index+1]]
        index += 4
    return opcodes

f = open("/Users/igor/Programowanie/advent-of-code-2019/2/input.txt", "r")
lines = f.readlines()
opcodes = []
for op in lines[0].split(','):
    opcodes.append(int(op))
print(opcodes)
index = 0

# print(run(opcodes))

for noun in range(100):
    for verb in range(100):
        newOpcodes = copy.deepcopy(opcodes)
        newOpcodes[1] = noun
        newOpcodes[2] = verb
        #print(newOpcodes)
        output = runAndReturnOutput(newOpcodes)
        if(output == 19690720):
            print("noun = " + str(noun) + " verb = " + str(verb))






