# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

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
import numpy as np
#import scipy

class Lion:
    
    def __init__(self, id, row, col, dist):
        self.id = id
        self.row = row
        self.col = col
        self.dist = dist
        self.trespassCount = 0
        
    def incrementTrespass(self):
        self.trespassCount += 1
        
    def checkForTrespassers(self, listOfLions):
        for lion in listOfLions:
            if lion != self:
                x_dist = abs( self.row - getattr(lion, "row"))
                y_dist = abs( self.col - getattr(lion, "col"))
                m_dist = x_dist + y_dist
                if self.dist >= m_dist:
                    lion.incrementTrespass()
    



#dimensions of matrix
n = get_number()
m = get_number()
#number of lions
k = get_number()

lionList = []

for i in range(0, k):
    id = i + 1
    lionRow = get_number()
    lionCol = get_number()
    lionDist = get_number()
    lionList.append( Lion(id, lionRow, lionCol, lionDist) )
    
#savanna = [ [None for i in range(0, n)] for i in range(0, m)]

#print (np.array(savanna))
#if type(i, j) is Lion

for lion in lionList:
    lion.checkForTrespassers(lionList)
    
maxCount = 0
worstLion = None
for lion in lionList:
    #print (getattr(lion, "trespassCount"))
    if getattr(lion, "trespassCount") > maxCount:
        maxCount = getattr(lion, "trespassCount")
        worstLion = getattr(lion, "id")
        
print (str(worstLion) + " " + str(maxCount))