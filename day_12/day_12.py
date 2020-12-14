import numpy as np
from math import sin, cos, radians

def ReadCommands(filename):
    with open(filename,"r") as file:
        data = [line.strip("\n") for line in file.readlines()]
    return data

class Boat:
    def __init__(self):
        # Begins at (0,0) facing East
        self.position = ([0.0],[0.0])
        self.vector = ([1.0],[0.0])
        
    def __str__(self):
        return (f"position={self.position}, facing ={self.vector}")
        
    def rotate(self,direction,angle):
        # L turn right by given num of degrees 
        # R turn right by given num of degress
        if direction == "R":
            angle = -1.0*angle
        elif direction == "L":
            angle = 1.0*angle
        else:
            print(f"Rotation {direction+angle} not recognised")
        
        rot = ([cos(radians(angle)), -sin(radians(angle))],
                [sin(radians(angle)),cos(radians(angle))])
        
        self.vector = np.matmul(rot,self.vector)
        
    def command(self,command):
        order = command[0]
        value = float(command[1:])
        # N move north (0,1)
        if order == "N":
            self.position = np.add(  np.dot(value,([0.0],[1.0])),self.position)
        # S move south (0,-1)
        elif order == "S":
            self.position = np.add(  np.dot(value,([0.0],[-1.0])),self.position)
        # E move east (1,0)
        elif order == "E":
            self.position = np.add(  np.dot(value,([1.0],[0.0])),self.position)
        # W move west (-1,0)
        elif order == "W":
            self.position = np.add(  np.dot(value,([-1.0],[0.0])),self.position)
        # F move forward in current facing by given value
        elif order == "F":
            self.position = np.add(  np.dot(value,self.vector),self.position)
        elif order == "R" or order == "L":
            self.rotate(order,value)
            
    def manhattandist(self):
        return self.position
            

if __name__=="__main__":
    data = ReadCommands("input.txt")
    ferry = Boat()
    for item in data:
        #print(item)
        ferry.command(item)
        #print(ferry)
    print(f"Manhattan Distance = {abs(ferry.position[0][0])+abs(ferry.position[1][0])}")
        
    
    