
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
import scipy

d = get_number()
dims = [1, 1, 1, 1, 1]

for i in range(0, d):
    dims[i] = (get_number())
    
dataList = list(input().split(' '))
#print (dataList)
    
npt = np.array( [[[[[ int(dataList.pop(0)) for i in range(0, dims[len(dims)-1]) ] for j in range(0, dims[len(dims)-2]) ] for k in range(0, dims[len(dims)-3]) ] for l in range(0, dims[len(dims)-4]) ]  for m in range(0, dims[len(dims)-5]) ] )
    
#print (npt)
    



#tesseract = np.zeros(tuple((dims)))
#print (tesseract)


#for i in range(0, d):
#    for j in range(0, dims[i]):


#npt = np.zeros(tuple(reversed(dims)))

#tesseract = [ [ [ [ [None for a in range(dims[0]) ] for b in range(dims[1]) ] for c in range(dims[2]) ] for d in range(dims[3])] for e in range(dims[4]) ]

#npt = np.array( tesseract )
#tesseract = [ [ [ [ [None] * dims[0]  ] * dims[1] ] * dims[2] ] * dims[3] ] * dims[4]

#iterate over all the dimensions, backwards
#for every last dimension
#for i in range(0, dims[len(dims)-1]):
    #and for every next
#    for j in range(0, dims[len(dims)-2]):
#        for k in range(0, dims[len(dims)-3]):
#            for l in range(0, dims[len(dims)-4]):
#                for m in range(0, dims[len(dims)-5]):
#                    npt[i][j][k][l][m] = get_number()

#npt = np.array( [[[[[ get_number() for i in range(0, dims[len(dims)-1]) ] for j in range(0, dims[len(dims)-2]) ] for k in range(0, dims[len(dims)-3]) ] for l in range(0, dims[len(dims)-4]) ]  for m in range(0, dims[len(dims)-5]) ] )
#npt = np.array(tess)
#print (npt.reshape(1,1,1,3,3))


#for every query

queries = get_number()

for q in range(0, queries):
    
    t1_list = []
    t2_list = []
    for i in range(0, d):
        t1_list.append(get_number() - 1)
        
    for i in range(0, d):
        t2_list.append(get_number() - 1)
        
    while(len(t1_list) < 5):
        t1_list.append(0)
        
    while(len(t2_list) < 5):
        t2_list.append(0)
        
    t1 = tuple((t1_list))
    t2 = tuple((t2_list))
    
    #print (t1)
    #print (t2)
    
    result = npt[ t1[0] : t2[0] + 1, t1[1] : t2[1] + 1, t1[2] : t2[2] + 1, t1[3] : t2[3] + 1, t1[4] : t2[4] + 1 ]
    #print (result)
    resultSum = result.sum()
    #print (npt[ 0:0 ])
    
    print (int(resultSum))
















"""
#print (tesseract)
#for every query

queries = get_number()

for q in range(0, queries):
    
    t1_list = []
    t2_list = []
    for i in range(0, d):
        t1_list.append(get_number())
        
    for i in range(0, d):
        t2_list.append(get_number())
        
    while(len(t1_list) < 5):
        t1_list.append(1)
        
    while(len(t2_list) < 5):
        t2_list.append(1)
        
    t1 = tuple(t1_list)
    t2 = tuple(t2_list)
    
    result = 0
    
    #print (t1)
    #print (t2)
    
    
    #iterate over all the dimensions, backwards
    #for every last dimension
    for i in range(t1[4], t2[4]+1):
        #and for every next
        for j in range(t1[3], t2[3]+1):
            for k in range(t1[2], t2[2]+1):
                for l in range(t1[1], t2[1]+1):
                    for m in range(t1[0], t2[0]+1):
                        result += tesseract[i-1][j-1][k-1][l-1][m-1]
                        #print ("Calculating: " + str( tesseract[i-1][j-1][k-1][l-1][m-1] ))
                        
    

    print (result)
"""