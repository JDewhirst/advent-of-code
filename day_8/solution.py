import re

def ReadDocuments(filename):
    with open(filename,"r") as file:
        data = [line.strip("\n").split() for line in file.readlines()]
    return data
    
def ExecCommand(data,i,acc):
    # nop : does nothing
    # acc : increases accumulator 
    # jmp : moves position
    if data[i][0] == "nop":
        i += 1
    elif data[i][0] == "acc":
        acc += int(data[i][1])
        i += 1
    elif data[i][0] == "jmp":
        i += int(data[i][1])
    #print(f"i={i} acc={acc}")
    return i, acc
    
def FindLoop(data):
    acc = 0
    i = 0
    visited_commands = set()
    while i < len(data):
        if i in visited_commands:
            return acc, True
        visited_commands.add(i)
        i, acc = ExecCommand(data,i,acc)
    return acc, False
    
def FixLoop(data):
    i = 0
    while i < len(data)-1:
        data[i][0] = Flip(data[i][0])
        acc, result = FindLoop(data)
        #print(i, data)
        if result == False:
            return acc, i, data
        data[i][0] = Flip(data[i][0])
        i += 1
        
    return acc, i, data
    
def Flip(command):
    if command == "nop":
        command = "jmp"
    elif command == "jmp":
        command = "nop"
    return command
    
if __name__=="__main__":
    data = ReadDocuments("input.txt")
    acc, Loop = FindLoop(data)
    print(f"Part 1: acc = {acc} Loop = {Loop}")
    if Loop:
        acc2, i, data = FixLoop(data)
        print(f"Part 2: acc = {acc2} Altered Line = {i}")
        