def ReadBP(filename):
    with open(filename,"r") as file:
        data = {line for line in file.read().splitlines()}
    return data
    
def GetIDS(BoardingPasses):
        return {int(item.translate(str.maketrans("FBLR","0101")),2) for item in BoardingPasses}
    
def MySeat(SeatIDs):
        return set(range(min(SeatIDs),max(SeatIDs))) - SeatIDs