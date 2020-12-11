import itertools

def ReadDocuments(filename):
    with open(filename,"r") as file:
        data = sorted([int(line.strip("\n")) for line in file.readlines()])
    return data

def AllAdaptDiffs(data):
    device_joltage = data[-1]+3
    diff = [data[0]]
    for i in range(1,len(data)):
        diff.append(data[i]-data[i-1])
    diff.append(device_joltage-data[i])       
    return diff  
    
def WaysTo(arr, x):
    if x in arr:
        return arr[x]
    else:
        return 0
    
if __name__=="__main__":
    data = ReadDocuments("input.txt")
    diff = AllAdaptDiffs(data)
    a = diff.count(1)
    b = diff.count(3)
    print(f"1-jolt diff={a}, 3-jolt diff={b}")
    print(f"Number of 1-jolt diff multiplied by number of 3-jolt diff={a*b}")
    
    arr = {}
    arr[0] = 1
    for item in data:
        arr[item] = WaysTo(arr, item-1) + WaysTo(arr, item-2) + WaysTo(arr, item-3)

    print(f"Number of possible arrangements = {arr[max(data)]}")