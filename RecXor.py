import sys
import math

import sys
import math

lines = [x for x in sys.stdin]
tc = int(lines[0])

#returns xor of range from 0 to a
def xorRange(a):
	if (a % 4) == 0:
		return a
	elif (a % 4) == 1:
		return 1
	elif (a % 4) == 2:
		return (a + 1)
	else:
		return 0

def f(a):
     res = [a, 1, a+1, 0]
     return res[a%4]

def getXor(a, b):
	return f(b) ^ f(a-1)



for iterate in range(tc):
	in_line = lines[iterate+1]
	vals = [int(x) for x in in_line.strip().split(" ")]
	l = vals[0]
	h = vals[1]
	n = vals[2]
	d1 = vals[3]
	d2 = vals[4]


	inner_corner_top = [(d1-n)%l,(d1-n)//l]
	inner_corner_bottom = [(d2-n)%l,(d2-n)//l]
	
	if inner_corner_top[0] > inner_corner_bottom[0]:
	    inner_corner_top,inner_corner_bottom = inner_corner_bottom,inner_corner_top
	if inner_corner_top[1] > inner_corner_bottom[1]:
	    inner_corner_top[1],inner_corner_bottom[1] = inner_corner_bottom[1],inner_corner_top[1]
	
	left_border = min([inner_corner_top[0],inner_corner_bottom[0]])
	right_border = max([inner_corner_top[0],inner_corner_bottom[0]])

	top_left = (left_border,inner_corner_top[1])
	top_right = (right_border,inner_corner_top[1])

	xors = []
	last_border = n
	for i in range(inner_corner_top[1],inner_corner_bottom[1]+1):
		xors.append(getXor(last_border,(l*i)+n+left_border-1))
		last_border = (l*i)+n+right_border+1
	xors.append(getXor(last_border,l*h+n-1))
	xor1 = xors[0]
	for xor in xors[1:]:
		xor1 = xor1^xor

	print(xor1)



