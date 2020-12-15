
def Read(filename):
    with open(filename, "r") as file:
        timestamp =  file.readline().strip('\n')
        buses = file.readline().strip().split(",")
        #buses[-1] = buses[-1].strip('\n')
    return int(timestamp), buses
    
# for each bus timestamp % ID
# next bus after timestamp = timestamp+(ID-timestamp%ID)
def nextbus(timestamp,data):
    return [int(data[i]) - timestamp % int(data[i]) for i in range(len(data))]
    
if __name__=="__main__":
    timestamp, buses = Read("input.txt")
    
    ### part 1
    no_x_buses = []
    for bus in buses:
        if bus == "x":
            continue
        else:
            no_x_buses.append(int(bus))
    a = nextbus(timestamp,no_x_buses)
    print(f"Part 1: Wait {min(a)}min for bus ID {no_x_buses[a.index(min(a))]}")
    print(f"Result 1 = {min(a)*no_x_buses[a.index(min(a))]}")
    
    ### part 2
    # create pairs of (divisor, remainder) for every available bus
    buses = [(int(buses[i]), (int(buses[i]) - i) % int(buses[i]))
        for i in range(len(buses)) if buses[i] != 'x']
    result = 0
    increment = 1

    for bus in buses:
        while result % bus[0] != bus[1]:
            result += increment
        increment *= bus[0]

    print("Part 2")
    print(f"Result 2 {result}")
    