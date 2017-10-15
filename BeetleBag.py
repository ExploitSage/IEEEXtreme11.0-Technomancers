import sys

#All Stdin at once!
data = sys.stdin.readlines()

cases = int(data.pop(0))

def fill_bag(gadget,stowed,usage,power):
    if usage+gadget[0] <= capacity:
        usage += gadget[0]
        power += gadget[1]
        stowed.append(gadget)
    else:
        back_fill = fill_bag(gadget,stowed[:-1],usage-stowed[-1][0],power-stowed[-1][1])
        if back_fill[3] >= power:
            gadget,stowed,usage,power = back_fill
        else:
            forward_fill = fill_bag(gadget,stowed[1:],usage-stowed[0][0],power-stowed[0][1])
            if forward_fill[3] >= power:
                gadget,stowed,usage,power = forward_fill
    return (gadget,stowed,usage,power)

for case in range(cases):
    capacity, lengadgets = [int(x) for x in data.pop(0).split()]
    gadgets = sorted([[int(x) for x in data.pop(0).split()] for gadget in range(lengadgets)], key=lambda x: x[1]/x[0], reverse=True)
    
    usage = 0
    power = 0
    stowed = []
    
    # print gadgets
    
    for gadget in gadgets:
        if gadget[0] < capacity:
            gadget,stowed,usage,power = fill_bag(gadget,stowed,usage,power)
    # print stowed
    print power