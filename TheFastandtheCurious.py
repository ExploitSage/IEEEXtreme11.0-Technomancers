import sys
lines = [x.strip() for x in sys.stdin]

nodes = {}

bad_nodes = []
def recursive_search(original,source,parent,visited_nodes):
        visited_nodes = visited_nodes[:]
        visited_nodes.append(source)
        for n_dest in nodes[source]:
                if n_dest != parent:
                        if n_dest == original:
                                bad_nodes.extend(visited_nodes)
                                return True
                        if n_dest in visited_nodes:
                                continue
                        if recursive_search(original,n_dest,source,visited_nodes):
                                return True
        return False


num_nodes = int(lines[0].split(" ")[0])
nodes = {(x+1):[] for x in range(num_nodes)}
for link in lines[1:]:
	link = link.split(" ")
	nodeA = int(link[0])
	nodeB = int(link[1])
	nodes[nodeA].append(nodeB)
	nodes[nodeB].append(nodeA)


end_nodes = []
for n in nodes:
	if len(nodes[n]) < 2:
		end_nodes.append(n)

ok_nodes = []
maybe_nodes = {}
for n in end_nodes:
	cur_node = n
	chain_of_nodes = []
	while len(nodes[cur_node]) < 3:
		ok_nodes.append(cur_node)
		chain_of_nodes.append(cur_node)
		next_node = [x for x in nodes[cur_node] if x not in chain_of_nodes]
		if len(next_node) == 0:
			break
		next_node = next_node[0]
		if len(nodes[next_node])>2:
			if next_node in maybe_nodes:
				maybe_nodes[next_node].append(cur_node)
			else:
				maybe_nodes[next_node] = [cur_node]
		cur_node = next_node

for n in maybe_nodes:
	if len(nodes[n])<=len(maybe_nodes[n])+1:
		ok_nodes.append(n)
		for connected_node in nodes[cur_node]:
			cur_node = connected_node
			chain_of_nodes = []
			while len(nodes[cur_node]) < 3:
				ok_nodes.append(cur_node)
				chain_of_nodes.append(cur_node)
				next_node = [x for x in nodes[cur_node] if x not in chain_of_nodes][0]

ok_nodes = [x for x in set(ok_nodes)]
for i in sorted(ok_nodes):
	print(i)
		

		





