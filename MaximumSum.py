import sys

#All Stdin at once!
data = sys.stdin.readlines()

cases = int(data.pop(0))


def reoptimize( sortedList ):
    #for i in reversed(sortedList):
        #if i in sortedList[ 0, int(len(sortedList)/2) ]:
    for i in range(0, len(sortedList) ):
        if sortedList[i] == 0:
            del sortedList[i]
            sortedList.insert(0, 0)
            #print ("Working: " + str(sortedList))
        if sortedList[i] == 1:
            if ( i > 0 and sortedList[ i - 1 ] == 1):
                newIn = sortedList.index(1)
                del sortedList[i]
                sortedList.insert(newIn, 1)
            
    return sortedList
            





for case in range(cases):
    num = int(data.pop(0))
    values = sorted([int(x) for x in data.pop(0).split()])[::-1]
    out = []
    out2 = []
    before = None
    

    #gustave's original function
    for x in values:
        if before == None:
            out.append(x)
            before = True
        else:
            if before == True:
                out.append(x)
                before = False
            else:
                out.insert(0, x)
                before = True
                
        #print (out)
        
    before = None
               
    #my addition 
    for x in values:
        if before == None:
            out2.append(x)
            before = True
        else:
            if before == True:
                out2.insert(0, x)
                before = False
            else:
                out2.append(x)
                before = True
        
        #print (out2)
                
    out = reoptimize(out)
    out2 = reoptimize(out2)
    
    #print out
    #print out2
                
    for i in range(0, len(out)):
        if (out[i] > out2[i]): #out2 is better lexocog.
            out = out2
            break
        elif (out[i] < out2[i]):
            break
    
    print sum([out[i]*out[i+1] for i in range(len(out)-1)])
    print " ".join(map(str, out))
