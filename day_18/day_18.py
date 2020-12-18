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

def Operation(result, number, operator):
    if result == None:
        return number
    elif operator == "*":
        result *= number
    elif operator == "+":
        result += number
    return result
   
def Evaluate(line, position):
    # iterate through string
    result = None
    operator = None
    number = None
    i = position
    while i < len(line):
        character = line[i]
        #print(i, character, result)
        if character == " ":
            i += 1
            pass
        elif character == "(":
            i, paren_result = Evaluate(line,i+1)
            result = Operation(result, paren_result, operator)
        elif character == "*" or character == "+":
            operator = character
            i += 1
        elif num.match(character):
            number = int(character)
            if not result:
                result = int(character)
            else:
                result = Operation(result, number, operator)
                operator = None
            i += 1
        elif character == ")":
            return i+1, result
            
    return result
        
    
if __name__=="__main__":
    filename = "input.txt"
    data = Read(filename)
    part_1_result = 0
    for line in data:
        #print(line)
        part_1_result += Evaluate(line,0)
        
    print(f"Part 1: Sum of all expressions = {part_1_result}")