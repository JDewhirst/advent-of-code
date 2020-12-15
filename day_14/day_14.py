
def Part1(filename):
    file = open(filename,mode='r')
    mem = {}
    for line in file.read().split("\n"):
        if "mask" in line:
            mask = line.split(" = ")[1]
            continue
        else:
            mem_helper, value = line.split(" = ")
            mem_helper = mem_helper.replace("[",",")
            mem_helper = mem_helper.replace("]","")
        # Convert to Value to Binary 36b
        value = f"{int(value):036b}"
        
        for i in range(len(value)):
            if mask[i] == "X" or mask[i] == value[i]: continue
            else:
                value = value[:i] + mask[i] + value[i+1:]
                
        # Allocate to MemoryError
        mem[mem_helper.split(",")[1]] = int(str(value),2)
        
    return sum(mem.values())

if __name__=="__main__":
    print( f"Part 1 = {Part1('input.txt')}" )