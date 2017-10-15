import sys

#All Stdin at once!
data = sys.stdin.readlines()

rows,cols,iterations = [int(x) for x in data.pop(0).split()]
rows -= 1
cols -= 1

board = [line[:-1] for line in data]

for interation in range(iterations):
    new_board = [['' for y in range(cols+1)] for x in range(rows+1)]
    for row in range(rows+1):
        new_row = ""
        for col in range(cols+1):
            neighbors = 0
            # Above
            offset_row = row-1 if  row-1 > -1 else rows
            neighbors += 1 if board[offset_row][col-1] == '*' else 0
            neighbors += 1 if board[offset_row][col] == '*' else 0
            neighbors += 1 if board[offset_row][col+1 if col+1 <= cols else 0] == '*' else 0
            # Below
            offset_row = row+1 if  row+1 <= rows else 0
            neighbors += 1 if board[offset_row][col-1] == '*' else 0
            neighbors += 1 if board[offset_row][col] == '*' else 0
            neighbors += 1 if board[offset_row][col+1 if col+1 <= cols else 0] == '*' else 0
            # Sides
            neighbors += 1 if board[row][col-1] == '*' else 0
            neighbors += 1 if board[row][col+1 if col+1 <= cols else 0] == '*' else 0
            
            if neighbors < 2 or neighbors > 3:
                new_row += '-'
            elif neighbors == 3:
                new_row += '*'
            else:
                new_row += board[row][col]
        new_board[row] = new_row
    board = new_board

for row in board:
    print row