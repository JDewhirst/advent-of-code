
def Read(filename):
    with open(filename, "r") as file:
        timestamp =  file.readline().strip('\n')
        buses = file.readline().split(",")
        buses[-1] = buses[-1].strip('\n')
    return int(timestamp), buses
    
# for each bus timestamp % ID
# next bus after timestamp = timestamp+(ID-timestamp%ID)
def nextbus(timestamp,data):
    return [int(data[i]) - timestamp % int(data[i]) for i in range(len(data))]
    
if __name__=="__main__":
    timestamp, buses = Read("input.txt")
    no_x_buses = []
    for bus in buses:
        if bus == "x":
            continue
        else:
            no_x_buses.append(int(bus))
    a = nextbus(timestamp,no_x_buses)
    print(f"Part 1: Wait {min(a)}min for bus ID {no_x_buses[a.index(min(a))]}")
    print(f"Result = {min(a)*no_x_buses[a.index(min(a))]}")
    
    
    