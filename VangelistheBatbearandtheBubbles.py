import sys
lines = [x.strip() for x in sys.stdin]

visited_nodes = []
nodes = {}

def recursive_search(source,parent):
        visited_nodes.append(source)
        for n_dest in nodes[source]:
                if n_dest != parent:
                        if n_dest in visited_nodes and n_dest != parent:
                                return True
                        if recursive_search(n_dest,source):
                                return True
        return False



for iteration in range(int(lines[0])):
        visited_nodes = []
        nodes = {x:[] for x in range(int(lines[(iteration*2)+1].split(" ")[0]))}
        connections = [int(x) for x in lines[(iteration*2)+2].split(" ")]
        for link_index in range(0,len(connections),2):
                nodes[connections[link_index]].append(connections[link_index+1])
                nodes[connections[link_index+1]].append(connections[link_index])

        had_loop = False
        for n in nodes:
                visited_nodes = []
                if recursive_search(n,None):
                        had_loop = True
                        break
        print(1 if had_loop else 0)