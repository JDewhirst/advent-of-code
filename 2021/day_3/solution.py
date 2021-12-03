def readData(filename):
    with open(filename) as f:
        data = f.readlines()
    data = [list(item.strip("\n")) for item in data]
    
    return data

def CountBits(input):
    bits = len(input[0])
    bitCount = [0 for i in range(bits)]
    for entry in input:
        for i in range(len(bitCount)):
            bitCount[i] += int(entry[i])
    return bitCount

def FindRates(bitCount, numEntries):
    gammaRate = [ '0' for i in range(len(bitCount)) ]
    
    for i in range(len(bitCount)):
        if bitCount[i] > numEntries/2:
            gammaRate[i] = '1'
    epsilonRate = ['0' if i == '1' else '1' for i in gammaRate]
    print(gammaRate, epsilonRate)

    return (''.join(gammaRate),''.join(epsilonRate))

def BinaryToDecimal(num, expo=1):
    if num== 0:
        return 0
    else:
        digit= num % 10
        num= int(num / 10)
        digit= digit * expo
        return digit + BinaryToDecimal(num, expo * 2)

if __name__=="__main__":
    input = readData("input.txt")
    for item in input:
        print(item)
    numEntries = len(input)
    bitCount = CountBits(input)
    print(bitCount)
    rates = FindRates(bitCount, numEntries)
    print(f'Gamma Rate = {BinaryToDecimal(int(rates[0]))}, Epsilon Rate = {BinaryToDecimal(int(rates[1]))};  Solution {BinaryToDecimal(int(rates[0])) * BinaryToDecimal(int(rates[1]))}')
    
