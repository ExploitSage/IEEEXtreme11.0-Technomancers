import sys

#All Stdin at once!
data = sys.stdin.readlines()

s = data.pop(0).strip()
srev = s[::-1]
num = int(data.pop(0))

for query in data:
    query = query.strip()[::-1]
    last_index = 0
    matches = 0
    for char in query:
        if char in srev[last_index:]:
            matches += 1
            last_index = srev.index(char)+1
        else:
            break
    print matches
