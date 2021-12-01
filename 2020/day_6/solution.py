import re

def ReadDocuments(filename):
    with open(filename,"r") as file:
        data = [re.sub('\n',' ', line) for line in file.read().split("\n\n")]
    return data
    
def SumGroupUniqueAnswers(data):
    num_unique_answers = 0
    for group in data:
        group_set = set()
        for character in group:
            if character == " ":
                pass
            elif character not in group_set:
                group_set.add(character)
        num_unique_answers += len(group_set)
    return num_unique_answers
    
def SumGrpUnanAnsw(data):
    num_group_unanimous = 0
    a = [line.split() for line in data]
    count = 0
    for group in a:
        for character in group[0]:
            CharInAll = True
            for i in range(1, len(group)):
                if character not in group[i]:
                    CharInAll = False
                    break
            if CharInAll == True:
                count += 1
    return count
    
        
        
        
    return 0

if __name__=="__main__":
    data = ReadDocuments("input.txt")
    print(f"Part 1: {SumGroupUniqueAnswers(data)}")
    print(f"Part 2: {SumGrpUnanAnsw(data)}")
   