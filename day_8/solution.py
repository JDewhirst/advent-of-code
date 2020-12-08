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
    
if __name__=="__main__":
    data = ReadDocuments("input.txt")
    acc = 0
    i = 0
    visited_commands = set()
    while i < len(data)-1:
        #print(f"i={i} set={visited_commands}")
        if i in visited_commands:
            print(f"Part 1: {acc}")
            break
        visited_commands.add(i)
        i, acc = ExecCommand(data,i,acc)
        