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
import random
"""
n = get_number()
m = get_number()
p = get_number()

class tile:
    
    def __init__(i, j, runnability, elevation):
        self.i = i
        self.j = j
        self.runnability = runnability
        self.elevation = elevation
        """
        #BELIEVE
a = get_number()
b = get_number()
print (random.randint(0, b*a))