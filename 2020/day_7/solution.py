import re

def ReadRules(filename):
    with open(filename, 'r') as file:
        r = re.compile(r"[0-9]+\s[a-z]+\s[a-z]+")
        data = {}
        for line in file:
            if not re.search(r"\sno\s", line):
                data[line[:line.index("bags") - 1]] = [[(bag[2:], int(bag[:1])) for bag in re.findall(r, line)], None]
            else:
                data[line[:line.index("bags") - 1]] = [[('', 0)], None]
    return data
    
# how many colours can, eventually, contain at least one shiny gold bag ?
def ContainsGold(data, name: str) -> bool:
    if data[name][0][0][1] == 0:
        return False
    elif data[name][1] is True:
        return True
    elif data[name][1] is False:
        return False
    contains: bool = False
    for (subname, subcount) in data[name][0]:
        if subname == "shiny gold":
            data[name][1] = True
            return True
        else:
            contains = contains or ContainsGold(data, subname)
    data[name][1] = contains
    return contains
    
def BagsInside(data, name: str) -> int:
    if data[name][0][0][1] == 0:
        return 0
    count = 0
    for (subname, subcount) in data[name][0]:
        count += subcount + subcount * BagsInside(data, subname)
    return count

if __name__=="__main__":
    data = ReadRules("input.txt")
    print(f"Part 1: {sum([ContainsGold(data, bag) for bag in data])}")
    print(f"Part 2: {BagsInside(data, 'shiny gold')}")

