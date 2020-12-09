import itertools

def ReadDocuments(filename):
    with open(filename,"r") as file:
        data = [int(line.strip("\n")) for line in file.readlines()]
    return data
    
def FindInvalid(data,preamble_length):
    i = preamble_length
    while i < len(data):
        a = [x for x in range(i-preamble_length,i)]
        is_sum = False 
        for j, k in itertools.combinations_with_replacement(a,2):
            if j != k and (data[j]+data[k] == data[i]):
            #print(f"i={i}={data[i]} j={j}={data[j]} k={k}={data[k]} sum j+k ={data[j]+data[k]}" )
                if data[j]+data[k] == data[i]:
                    is_sum = True
                if is_sum: break
        
        if not is_sum:
            return i, data[i]
        else:
            i += 1
            

    

if __name__=="__main__":
    # example.txt has a length 5 preamble and considers the 5 previous numbers
    # input.tt has a length 25 preamble and considers the 25 previous numbers
    data = ReadDocuments("input.txt")
    line, value = FindInvalid(data,25)
    print(f"First invalid value = {value}")
    
        