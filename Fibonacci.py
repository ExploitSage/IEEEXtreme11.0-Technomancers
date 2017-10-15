
# a simple parser for python. use get_number() and get_word() to read
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
import numpy
import scipy

import functools

@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

#fibDict = {}
#fibDict[0] = 0
#fibDict[1] = 1

t = get_number()


for x in range(0, t):
        
    n = get_number()
    
    n = n % 60
    
    print (fib(n + 1) % 10)