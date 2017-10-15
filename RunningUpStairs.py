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
import numpy
import scipy

fibList = [0, 1]

t = get_number()

for x in range(0, t):

    n = get_number()
    #print ("Solving " + str(n))
    if ( n == 1):
        print ( 1 )
    elif len(fibList) > n + 1:
        #print ("In list:")
        print (fibList[n+1])
    else:
        i = len(fibList) - 1
        while(i <= n):
            fibList.append( fibList[-1] + fibList[-2] )
            #print (fibList)
            i += 1
        print (fibList[-1])