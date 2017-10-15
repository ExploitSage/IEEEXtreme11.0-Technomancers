import sys
import copy
# 1 is BOB
# 2 is us
tic_tac = [[None,None,None],[None,None,None],[None,None,None]]

bob_turns = []
min_turns = []
for line in sys.stdin:
	vals = line.split(" ")
	bob_turns.append((int(vals[0])-1,int(vals[1])-1))


def recursive_solve(turns,btc,tic_tac_copy):
	global min_turns
	global bob_turns

	if len(min_turns) != 0 and len(turns) >= len(min_turns):
		return
	found_move = False
	while not found_move:
		if tic_tac_copy[bob_turns[btc][0]][bob_turns[btc][1]] != 2:
			tic_tac_copy[bob_turns[btc][0]][bob_turns[btc][1]] = 1
			found_move = True
		else:
			btc+=1

		if btc >= len(bob_turns):
			return
	
	if bob_win(tic_tac_copy) == 1:
		min_turns = turns
		return
	
	for i in range(3):
		for j in range(3):
			if tic_tac_copy[i][j] == None:
				tic_tac_cp_cp = copy.deepcopy(tic_tac_copy)
				tic_tac_cp_cp[i][j] = 2
				if bob_win(tic_tac_cp_cp) != -1:
					turns_cp = turns[:]
					turns_cp.append((i+1,j+1))
					recursive_solve(turns_cp,btc+1,tic_tac_cp_cp)



def bob_win(tic_tac_copy):
	for i in range(3):
		if tic_tac_copy[i][0] == 1 and tic_tac_copy[i][1] == 1 and tic_tac_copy[i][2] == 1:
			return 1
		if tic_tac_copy[0][i] == 1 and tic_tac_copy[1][i] == 1 and tic_tac_copy[2][i] == 1:
			return 1
		if tic_tac_copy[i][0] == 2 and tic_tac_copy[i][1] == 2 and tic_tac_copy[i][2] == 2:
			return -1
		if tic_tac_copy[0][i] == 2 and tic_tac_copy[1][i] == 2 and tic_tac_copy[2][i] == 2:
			return -1

	if tic_tac_copy[0][0] == 1 and tic_tac_copy[1][1] == 1 and tic_tac_copy[2][2] == 1:
		return 1
	if tic_tac_copy[0][2] == 1 and tic_tac_copy[1][1] == 1 and tic_tac_copy[2][0] == 1:
		return 1
	if tic_tac_copy[0][0] == 2 and tic_tac_copy[1][1] == 2 and tic_tac_copy[2][2] == 2:
		return -1
	if tic_tac_copy[0][2] == 2 and tic_tac_copy[1][1] == 2 and tic_tac_copy[2][0] == 2:
		return -1

	return 0
		
		
recursive_solve([],0,tic_tac[:])
for t in min_turns:
	print(str(t[0]) + " " + str(t[1]))

