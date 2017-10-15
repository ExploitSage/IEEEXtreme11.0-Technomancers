import sys
import math

lines = [x.strip() for x in sys.stdin]

dist = int(lines[0])

alpha_dict = {}
for l in lines[1:27]:
        vals = l.split(" ")
        angle = float(vals[1])

        alpha_dict[vals[0]] = (math.cos(math.radians(angle)) * dist, math.sin(math.radians(angle)) * dist)

message = lines[-1]

last_pos = (0,0)
tot_dist = 0
for i in message:
        let_val = ord(i)
        if let_val >= 97 and let_val <= 122:
                let_val -= 32
        if let_val >= 65 and let_val <= 90:
                char = chr(let_val)
                tot_dist += math.sqrt( (last_pos[0] - alpha_dict[char][0])**2 + (last_pos[1] - alpha_dict[char][1])**2)
                last_pos = (alpha_dict[char][0],alpha_dict[char][1])

print(math.ceil(tot_dist))
