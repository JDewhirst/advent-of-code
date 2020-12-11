from itertools import product

def ReadDocuments(filename):
    with open(filename,"r") as file:
        data = [list(line.strip("\n")) for line in file.readlines()]
    return data

def SeatRound(data):
    n = len(data)
    m = len(data[0])
    Next_Round = [["" for x in range(m)] for y in range(n)]

    for i, j in product(list(range(n)),list(range(m))):
        if data[i][j] == ".":
            Next_Round[i][j] = data[i][j]
        else:
            count = CountNeighbours(i,j,data,n,m)
            Next_Round[i][j] =  UpdateSpace(data[i][j],count)
        
    return Next_Round
    
def CountNeighbours(i,j,data,n,m):
    count = 0
    for k, l in product([-1,0,1],[-1,0,1]):
        if (i+k < 0 or j+l < 0 or i+k >= n or j+l >= m or
            (k == 0 and l == 0)):
            count += 0
        elif data[i+k][j+l] == "#":
            count += 1
            
    return count
       
def UpdateSpace(space,count):
    if space == ".":
        return space
    elif space == "L" and count == 0:
        # if no adjacent occupied seats seat becomes occupied
        return "#"
    elif space == "#" and count >= 4:
        return "L"
    else:
        return space
  
    
if __name__=="__main__":
    prev = ReadDocuments("input.txt")
    cur = SeatRound(prev)
    while prev !=  cur:
        a = SeatRound(cur)
        prev = cur
        cur = a
    count = 0
    for line in cur:
        count += line.count("#")
    #print(cur)
    #print(prev)
    print(count)
    