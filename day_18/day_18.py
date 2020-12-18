import re
### Calculator

## Expressions
# + addition
# * multiplication
# (...) parentheses

## Order precedence
# Operators have the same precedence, and are evaluated left to right
# Expressiosn withinn parentheses must be evaluated before being
# used in the surrounded expression

## Examples
# 1 + 2 * 3 = 9
# 1 + (2 * 3) = 7

def Read(filename):
    with open(filename,"r") as file:
        data = file.readlines()
    return [line.strip() for line in data]
   
num =  re.compile("[0-9]")
mul =  re.compile("\*")
add = re.compile("\+")
begin_paren = re.compile("\(")
end_paren = re.compile("\)")
   
def Evaluate(line):
    # iterate through string
    result = None
    i = 0 
    for i in range(len(line)):
        character = line[i]
        print(i, character, result)
        if character == " ":
            pass
        elif character == "*" or character == "+":
            opp = character
        elif num.match(character):
            number = int(character)
            if not result:
                result = int(character)
            else:
                if opp == "*":
                    result *= number
                elif opp == "+":
                    result += number
                opp = None
    return result
        
    
if __name__=="__main__":
    filename = "example.txt"
    data = Read(filename)
    results = []
    for line in data:
        results.append(Evaluate(line))
    
    print(f"Part 1: Sum of all expressions = {sum(results)}")