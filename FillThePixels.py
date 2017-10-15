# a simple parser for python. use get_number() and get_word() to read
import sys
sys.setrecursionlimit(900001)
def parser():
    while 1:
        try:
            data = list(input().split(' '))
            for number in data:
                if len(number) > 0:
                    yield(number) 
        except (EOFError):
            return

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
#import numpy as np
#import scipy
from copy import deepcopy

BLACK = 0
WHITE = 1

def plus(x, y):
    if ( (x < 0) or (y < 0) or (plusGrid[x][y] == BLACK) ):
        return
    else:
        plusGrid[x][y] = BLACK
        
        try:
            plus(x + 1, y)
        except (IndexError):
            pass
        
        try:
            plus(x - 1, y)
        except (IndexError):
            pass
        
        try:
            plus(x, y + 1)
        except (IndexError):
            pass    
        
        try:    
            plus(x, y - 1)
        except (IndexError):
            pass
        
        
def cross(x, y):
    if ( (x < 0) or (y < 0) or (crossGrid[x][y] == BLACK) ):
        return
    else:
        crossGrid[x][y] = BLACK
        
        try:
            cross(x - 1, y - 1)
        except (IndexError):
            pass
            
        try:
            cross(x + 1, y - 1)
        except (IndexError):
            pass
        
        try:
            cross(x + 1, y + 1)
        except (IndexError):
            pass
        
        try:    
            cross(x - 1, y + 1)
        except (IndexError):
            pass
        
def star(x, y):
    if ( (x < 0) or (y < 0) or (starGrid[x][y] == BLACK) ):
        return
    else:
        starGrid[x][y] = BLACK
        
        try:
            star(x+1, y)
        except (IndexError):
            pass
        
        try:            
            star(x-1, y)
        except (IndexError):
            pass
            
        try:    
            star(x, y+1)
        except (IndexError):
            pass
        
        try:            
            star(x, y-1)
        except (IndexError):
            pass
        
        try:            
            star(x+1,y+1)
        except (IndexError):
            pass
        
        try:            
            star(x-1, y-1)
        except (IndexError):
            pass
        
        try:            
            star(x-1, y+1)
        except (IndexError):
            pass
        
        try:            
            star(x+1,y-1)
        except (IndexError):
            pass
            
        try:
            star(x + 1, y)
        except (IndexError):
            pass


t = get_number()

#for every trial
for i in range(0, t):
    w = get_number() #width
    h = get_number() #height
    #print(w)
    #print("height: " + str(h))
    
    table = []
    #for every row
    for i in range(0, h):
        newRow = list(map(int, list( input() )))
        table.append(newRow)
        
    npt = table
    
    plusGrid = deepcopy(npt)
    crossGrid = deepcopy(npt)
    starGrid = deepcopy(npt)
    #print (plusGrid)
    #print (plusGrid[0][0])
    #print (plusGrid[0][1])
    #print (plusGrid[0][2])
    #print(plusGrid)
    results = [None, None, None]
    
    count = 0
    #iterate over plus grid
    for i in range(0, h):
        for j in range(0, w):
            #print (plusGrid[i][j])
            if plusGrid[i][j] == WHITE:
                #print ("yep, " + str(i) + " " + str(j))
                plus(i, j)
                #print (plusGrid)
                count += 1
    #print (count)
    results[0] = count
   
    count = 0
    #iterate over cross grid
    for i in range(0, h):
        for j in range(0, w):
            #print (plusGrid[i][j])
            if crossGrid[i][j] == WHITE:
                #print ("yep, " + str(i) + " " + str(j))
                cross(i, j)
                #print (plusGrid)
                count += 1
    #print (count)
    results[1] = count
    
    count = 0
    #iterate over star grid
    for i in range(0, h):
        for j in range(0, w):
            #print (plusGrid[i][j])
            if starGrid[i][j] == WHITE:
                #print ("yep, " + str(i) + " " + str(j))
                star(i, j)
                #print (plusGrid)
                count += 1
    #print (count)
    results[2] = count
    
    print ( str(results[0]) + " " + str(results[1]) + " " + str(results[2]) )
    
    
#plusGrid = np.array([[1] * 250] * 200)
#print (plusGrid)
#plus(0, 0)
#print (plusGrid)
    
    
    
    
    
    
    
    
    