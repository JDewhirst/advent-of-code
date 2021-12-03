def ReadData(filename):
    with open(filename) as f:
        data = f.readlines()
    return [item.split() for item in data]

def Part1EndLocation(course):
    position = 0
    depth = 0

    for command in course:
        #print(command)
        if command[0] == "forward":
            position += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
    return tuple([position, depth])

def Part2EndLocation(course):
    position = 0
    depth = 0
    aim = 0

    for command in course:
        #print(command)
        if command[0] == "forward":
            position += int(command[1])
            depth += aim*int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
    return tuple([position, depth])

if __name__=="__main__":
    course = ReadData("input.txt")
    part1Result = Part1EndLocation(course)
    part2Result = Part2EndLocation(course)
    print(f'Part 1: Position = {part1Result[0]}, Depth = {part1Result[1]}, Solution = {part1Result[0]*part1Result[1]}')
    print(f'Part 1: Position = {part2Result[0]}, Depth = {part2Result[1]}, Solution = {part2Result[0]*part2Result[1]}')
    