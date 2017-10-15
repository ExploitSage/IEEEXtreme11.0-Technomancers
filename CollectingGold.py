import sys



lines = [x.strip() for x in sys.stdin]
n = int(lines[0].split(" ")[0])


nodes = {}
for line in lines[1:n+1]:
	nodes[int(line)] = {}

for line in lines[n+1:]:
	vals = line.split(" ")
	nodeA = int(vals[0])
	nodeB = int(vals[1])
	nodes[nodeA][nodeB] = int(vals[2])
	nodes[nodeB][nodeA] = int(vals[2])


min_dist = float("inf")
max_gold = 0

start_node = min([x for x in nodes])
end_node = max([x for x in nodes])

def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

prime_list = []
product = 1
for x in gen_primes():
	product *= x
	prime_list.append(product)
	if(product > end_node):
		break


def getGold(node):
	for i,p in enumerate(prime_list):
		if p > node:
			break
	return i
		





queue = [
	[0,getGold(start_node),start_node,[start_node]] #Distance, gold, node, visited_nodes
	]

while queue:
	pathA = queue.pop(0)


	for destination in nodes[pathA[2]]:
		if destination not in pathA[3]:
			if destination == end_node:
				gold = pathA[1] + getGold(destination)
				distance = pathA[0] + nodes[destination][pathA[2]]
				if distance < min_dist:
					min_dist = distance
					max_gold = gold
				if distance == min_dist and gold > max_gold:
					min_dist = distance
					max_gold = gold
				continue

			visited = pathA[3] +[destination]
			new_path = [pathA[0]+nodes[destination][pathA[2]], pathA[1] + getGold(destination),destination,visited]
			queue.append(new_path)

	

	queue.sort()


	



print(max_gold)
