from itertools import product

def ReadDocuments(filename):
    with open(filename,"r") as file:
        data = [list(line.strip("\n")) for line in file.readlines()]
    return data

def SeatRound(data):
    Next_Round = [["." for x in range(m)] for y in range(n)]

    for i, j in product(list(range(n)),list(range(m))):
        if data[i][j] == ".":
            Next_Round[i][j] = data[i][j]
        else:
            count = CountNeighbours(i,j,data)
            Next_Round[i][j] =  UpdateSpace(data[i][j],count)
        
    return Next_Round
    
def CountNeighbours(i,j,data):
    count = 0
    if sight_line:
        for k, l in dirs:
            x = i + k
            y = j + l
            #print("####")
            #print(i,j,' ',x,y)
            while x >= 0 and y >= 0 and x < n and y < m :
                if data[x][y] == "#":
                    count += 1
                    break
                elif data[x][y] == "L":
                    count += 0
                    break
                x += k
                y += l
                #print(i,j,' ',x,y)
    else:
        for k, l in dirs:
            x = i + k
            y = j + l
            if (x < 0 or y < 0 or x > n-1 or y > m-1):
                count += 0
            elif data[x][y] == "#":
                count += 1
            
    return count
       
def UpdateSpace(space,count):
    if space == ".":
        return space
    elif space == "L" and count == 0:
        # if no adjacent occupied seats seat becomes occupied
        return "#"
    elif space == "#" and count >= vacate_threshold:
        return "L"
    else:
        return space
    
if __name__=="__main__":
    prev = ReadDocuments("input.txt")
    n = len(prev)
    m = len(prev[0])
    
    # Direction vectors
    dirs = [x for x in product([-1,0,1],[-1,0,1])]
    dirs.remove( (0,0) )
    
    # True = look for first seat they can see in each dir
    # False = only check immediate neighbours
    sight_line = True
    
    # occupied seat becomes empty if it has more neighbours than this
    vacate_threshold = 5
    
    cur = SeatRound(prev)
    while prev !=  cur:
        #print(cur)
        a = SeatRound(cur)
        prev = cur
        cur = a
        
    count = 0
    for line in cur:
        count += line.count("#")
    #print(cur)
    #print(prev)
    print(f"count = {count}")
    