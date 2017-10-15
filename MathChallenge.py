import sys
from math import factorial
#from scipy.misc import factorial

#All Stdin at once!
data = sys.stdin.readlines()

num = int(data.pop(0))

for test in data:
    a,b,c = [int(x) for x in test.split()]
    power = (factorial(b)/(factorial(c)*factorial(b-c)))
    print (a**power)%(1000000007)