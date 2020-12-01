def findtwo2020(filename):
    f = open(filename)
    data = f.readlines()
    f.close()
    data = [int(item.strip("\n")) for item in data]

    for i in range(len(data)):
        for j in range(i+1,len(data)):
            #print(data[i],data[j],data[i]+data[j])
            if data[i]+data[j] == 2020:
                return data[i]*data[j]
                
    return "Did not find it"
    
def findthree2020(filename):
    f = open(filename)
    data = f.readlines()
    f.close()
    data = [int(item.strip("\n")) for item in data]
    
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            for k in range(j+1,len(data)):
                #print(data[i]+data[j]+data[k])
                if data[i]+data[j]+data[k] == 2020:
                    return data[i]*data[j]*data[k]
    
    return "Did not find it"
