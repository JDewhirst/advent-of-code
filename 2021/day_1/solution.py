import re

def ReadData(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [int(item.strip("\n")) for item in lines]
    return lines

def NumOfIncreases(data):
    count = 0 
    for i in range(1,len(data)):
        if data[i-1] < data[i]:
            count +=1
    return count

def NumOfIncreasesWindow(data, window):
    count = 0
    for i in range(1,len(data)-window+1):
        #print(data[i:i+window])
        #print(data[i+window:i+window])
        if sum(data[i-1:i-1+window]) < sum(data[i:i+window]):
            count += 1
    return count

if __name__=="__main__":
    sonarReadings = ReadData("input.txt")
    print(f'Part 1: {NumOfIncreases(sonarReadings)}')
    print(f'Part 2: {NumOfIncreasesWindow(sonarReadings,3)}')

