import re

def ReadDocuments(filename):
    with open(filename,"r") as file:
        data = [re.sub('\n',' ', line) for line in file.read().split("\n\n")]
    return data
    
def NumValidFields(documents,authenticator):
    # Valid if all eight fields present
    # Valid if all fields except cid present
    # Invalid otherwhise
    # Returns num of passports with valid fields
    count = 0
    for doc in documents:
        field_set = set(re.findall("(.{3}?):",doc))
        for auth in authenticator:
            if field_set == authenticator[auth]:
                count += 1
                break
                
    return count
    
def NumValidDocuments(documents):
    byr = re.compile(r"\b(byr:(19[2-9]\d|200[0-2]))\b")
    iyr = re.compile(r"\b(iyr:(201\d|2020))\b")
    eyr = re.compile(r"\b(eyr:(202\d|2030))\b")
    hgt = re.compile(r"\b(hgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in))\b")
    hcl = re.compile(r"\b(hcl:#([0-9a-f]{6}))\b")
    ecl = re.compile(r"\b(ecl:(amb|blu|brn|gry|grn|hzl|oth))\b")
    pid = re.compile(r"\b(pid:(\d{9}))\b")
    
    return sum([all([re.search(x,passport) for x in [byr, iyr, eyr, hgt, hcl, ecl, pid]]) for passport in documents])
            
    
auth_fields = {
        "passport":{"byr","iyr","eyr","hgt","hcl","ecl","pid","cid"},
        "north pole credentials":{"byr","iyr","eyr","hgt","hcl","ecl","pid"}
    }