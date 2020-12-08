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
    for group in data:
        
    return 

   