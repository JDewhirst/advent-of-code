def ValidPasswords(filename):
    f = open(filename)
    data = f.readlines()
    f.close()
    data = [item.strip("\n").split() for item in data]
    
    num_valid = 0
    
    for entry in data:
        minimum, maximum = entry[0].split("-")
        
        given_letter = entry[1][0]
        password = entry[2]
        
        # count occurances of letter
        count = 0
        for letter in password:
            if given_letter == letter:
                count += 1
        if count >= int(minimum) and count <= int(maximum):
            num_valid += 1
            
    return num_valid