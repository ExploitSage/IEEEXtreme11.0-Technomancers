import sys

#All Stdin at once!
data = sys.stdin.readlines()

lodgings = [i for i in range(int(data.pop(0)))]

familys = [[int(x) for x in (family+" "+str(i)).split()] for i, family in enumerate(data)]

possibles = [[x for x in lodgings if x not in family] for family in familys]
possibles.sort(key=len)

deep = [] # 
spaces = [None for i in range(len(lodgings))]
remove = 0

def assign_family(family, index):
    found_space = False
    if len(family) > 0:
        for lodge in family:
            if spaces[lodge] != None:
                fam_in_lodge = possibles[spaces[lodge]]
                if spaces[lodge] not in deep:
                    deep.append(spaces[lodge])
                    if assign_family(fam_in_lodge[0:fam_in_lodge.index(lodge)]+fam_in_lodge[fam_in_lodge.index(lodge)+1:],spaces[lodge]):
                        spaces[lodge] = index
                        found_space = True
                        break;
                    deep.remove(spaces[lodge])
            else:
                spaces[lodge] = index
                found_space = True
                break;
    return found_space

to_place = []

for index,family in enumerate(possibles):
    if not assign_family(family, index):
        to_place.append(family)
        remove += 1

for i in range(20):
    for index,family in enumerate(possibles):
        if family in to_place:
            if assign_family(family, index):
                to_place.remove(family)
                remove -= 1

print remove
