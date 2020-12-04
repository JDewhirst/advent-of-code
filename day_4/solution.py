def ReadDocuments(filename):
    f = open(filename,"r")
    data = {}
    i = 0
    for line in f:
        if line == "\n":
            i+=1
        elif i in data:
            data[i] += line.strip("/n").split()
        else:
            data[i] = line.strip("/n").split()
    f.close()
    return data
    
def NumValidDocuments(documents,authenticator):
    # Valid if all eight fields present
    # Valid if all fields except cid present
    # Invalid otherwhise
    # Return num of valid passports
    count = 0
    for doc in documents:
        field_set = {field[0:3] for field in documents[doc]}
        for auth in authenticator:
            if field_set == authenticator[auth]:
                count += 1
                break
                
    return count
            
    
auth_fields = {
        "passport":{"byr","iyr","eyr","hgt","hcl","ecl","pid","cid"},
        "north pole credentials":{"byr","iyr","eyr","hgt","hcl","ecl","pid"}
    }
    