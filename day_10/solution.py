import itertools

def ReadDocuments(filename):
    with open(filename,"r") as file:
        data = sorted([int(line.strip("\n")) for line in file.readlines()])
    return data

def AllAdapterChain(data):
    device_joltage = data[-1]+3
    diff = [data[0]]
    for i in range(1,len(data)):
        diff.append(data[i]-data[i-1])
    diff.append(device_joltage-data[i])       
    return diff
    
if __name__=="__main__":
    data = ReadDocuments("input.txt")
    diff = AllAdapterChain(data)
    a = diff.count(1)
    b = diff.count(3)
    print(f"1-jolt diff={a}, 3-jolt diff={b}")
    print(f"Number of 1-jolt diff multiplied by number of 3-jolt diff={a*b}")