import sys

forest = []


lines = [x.strip() for x in sys.stdin]
r = int(lines[0].split(" ")[0])
c = int(lines[0].split(" ")[1])


for line in lines[1:]:
	vals = line.strip().split(" ")
	forest.append([int(x) for x in vals])




def calculate_min_health(min_health,sequence):
	summation = 0
	for s in sequence:
		summation += s
		if summation < min_health:
			min_health = summation
	return min_health
		
min_x = calculate_min_health(0,[forest[x][0] for x in range(r)])
g_min = calculate_min_health(min_x,[forest[r-1][x] for x in range(c)])
min_x2 = calculate_min_health(0,[forest[0][x] for x in range(c)])
g_min2 = calculate_min_health(min_x2,[forest[x][c-1] for x in range(r)])
max_hp = max([g_min,g_min2])
		
		

queue = [
	[forest[0][0],(0,0),forest[0][0]]	
	]
while queue:
	pathA = queue.pop(0)
	pathB = [pathA[0],pathA[1],pathA[2]]

	if pathA[0] <= max_hp:
		continue
	
	if pathA[1][0] != r-1:	
		new_A_pos = (pathA[1][0]+1,pathA[1][1])
		new_A_hp = pathA[2] + forest[new_A_pos[0]][new_A_pos[1]]
		if new_A_hp < pathA[0]:
			new_A_min = new_A_hp
		else:
			new_A_min = pathA[0]
		new_pathA = [new_A_min,new_A_pos,new_A_hp]
		queue.append(new_pathA)
	else:
		min_health = calculate_min_health(pathA[0],[forest[r-1][x] for x in range(pathA[1][1],c)])
		if min_health > max_hp:
			max_hp = min_health
		

	if pathB[1][1] != c-1:	
		new_B_pos = (pathB[1][0],pathB[1][1]+1)
		new_B_hp = pathB[2] + forest[new_B_pos[0]][new_B_pos[1]]
		if new_B_hp < pathB[0]:
			new_B_min = new_B_hp
		else:
			new_B_min = pathB[0]
		new_pathB = [new_B_min,new_B_pos,new_B_hp]
		queue.append(new_pathB)
	else:
		min_health = calculate_min_health(pathB[0],[forest[x][c-1] for x in range(pathB[1][0],r)])
		if min_health > max_hp:
			max_hp = min_health


	queue = sorted(queue,reverse=True)


	



print(1 if max_hp > 0 else (-max_hp) + 1)
