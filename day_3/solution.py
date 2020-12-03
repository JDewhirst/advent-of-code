def TreesOnSlope(x,y,filename):
    f = open(filename)
    data = f.readlines()
    f.close()
    data = [item.strip("\n") for item in data]
    n = len(data)
    m = len(data[0])
    num_trees = 0
    i = 1
    
    while i*y <= n-1:
        if data[i*y][i*x % (m)] == "#":
            num_trees += 1
        i += 1
            
    return num_trees