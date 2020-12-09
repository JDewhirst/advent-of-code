def ReadDocuments(filename):
    with open(filename,"r") as file:
        data = [int(line.strip("\n")) for line in file.readlines()]
    return data
    
def FindWeakness(data,preamble_length):
    i = preamble_length
    while i < len(data):
        is_sum = False 
        for j in range(i-preamble_length,i):
            for k in range(j+1,i):
                #print(f"i={i}={data[i]} j={j}={data[j]} k={k}={data[k]} sum j+k ={data[j]+data[k]}" )
                if data[j]+data[k] == data[i]:
                    is_sum = True
                    
        if not is_sum:
            return i, data[i]
        else:
            i += 1


if __name__=="__main__":
    # example.txt has a length 5 preamble and considers the 5 previous numbers
    # input.tt has a length 25 preamble and considers the 25 previous numbers
    data = ReadDocuments("input.txt")
    line, value = FindWeakness(data,25)
    print(value)
        