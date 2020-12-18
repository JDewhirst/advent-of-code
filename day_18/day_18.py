import re
### Calculator

def Read(filename):
    with open(filename,"r") as file:
        data = file.readlines()
    return [line.strip() for line in data]

### Part 1

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
   
# dumb solution
num =  re.compile("[0-9]")

def Operation(result, number, operator):
    if result == None:
        return number
    elif operator == "*":
        result *= number
    elif operator == "+":
        result += number
    return result
   
def Part1Eval(line, position):
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
    

# part 1 smart solution with regex
parens = re.compile(r'\(\s*(\d+)\s*\)')
operation = re.compile(r'(\d+)\s*([+*])\s+(\d+)')

def Eval(line):
    while True:
        line = re.sub(parens, r'\1', line)
        match = re.search(operation, line)
        if match:
            lhs, op, rhs = match.groups()
            if op == "+":
                value = int(lhs) + int(rhs)
            elif op == "*":
                value = int(lhs) * int(rhs)
            line = line[:match.start()] + str(value) + line[match.end():]
        else:
            break
    return int(line)

### Part 2
# Same rules as prior except that addition has precedence over
# multiplication
# def Part2Eval(line, position):
    
    
    
    # # So I believe that the sensible way to do this is to atomise
    # # if we have 1+2*3+4*5+6 we want to parse it like sort
    # # (1+2)*(3+4)*(5+6) 
    # # How do you do that ?
    # # Well. Regex ?
    # return False
        
    
if __name__=="__main__":
    filename = "input.txt"
    data = Read(filename)
    part_1_result = sum(map(Eval,data))
        
    print(f"Part 1: Sum of all expressions = {part_1_result}")