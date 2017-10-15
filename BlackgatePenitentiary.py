import sys

#All Stdin at once!
data = sys.stdin.readlines()

num = int(data.pop(0))

unsorted = [ [int(member.split()[1]),member.split()[0]] for member in data]
villans_sorted = sorted(unsorted, key=lambda x: x[0], reverse=False)

size = None
names = ""
start_index = 0
current_index = 0
for villian in villans_sorted:
    if size == None:
        size = villian[0]
        names = villian[1] + " "
    else:
        if size != villian[0]:
            names = " ".join(sorted(names.split()))+" "
            print names + str(start_index+1) + " " + str(current_index)
            start_index = current_index
            size = villian[0]
            names = villian[1] + " "
        else:
            names += villian[1] + " "
    current_index += 1
names = " ".join(sorted(names.split()))+" "
print names + str(start_index+1) + " " + str(current_index)