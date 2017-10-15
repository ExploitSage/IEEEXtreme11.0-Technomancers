import sys

lines = [x.strip() for x in sys.stdin]
original = [int(x) for x in lines[1].split(" ")]
q = int(lines[2])




def find_greater(l):
	arr_changed = False
	for i in range(len(l)-2,-1,-1):
		if min(l[i+1:]) > l[i]:
			for j in range(i,len(l)):
				if l[j]==min(l[i+1:]):
					break
			temp = l[i]
			l[i] = l[j]
			l[j] = temp
			arr_changed = True
			break
	if not arr_changed:
		i = -1
	return l,i

def find_lesser(l,i):
	for j in range(i+1,len(l)-1):
		if min(l[j+1:]) < l[j]:
			for k in range(j+1,len(l)):
				if k==min(l[j+1:]):
					break
			temp = l[j]
			l[j] = l[k]
			l[k] = temp
	return l

def cost(l1,l2):
	count = 0
	for i in range(len(l1)):
		if l1[i] != l2[i]:
			count+=1
	return count
for line in lines[3:]:
	vals = line.split(" ")
	lower = int(vals[0])-1
	higher = int(vals[1])
	
	a = original[lower:higher]

	new_a,index = find_greater(a[:])
	if index != -1:
		new_a = find_lesser(new_a,index)
	print(cost(a,new_a))

