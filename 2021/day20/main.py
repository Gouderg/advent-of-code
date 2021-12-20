
def init_board(size):
    return [['.' for i in range(0, size)] for j in range(size)]

# Extract data.
size = 500
algorithm = ""
board = init_board(size)
isOkey = True
i, j = 0, 0

with open('input.txt', 'r') as file:
    for row in file:
        if row == "\n":
            isOkey = False
        
        elif isOkey:
            algorithm = row.replace('\n', '')
        
        else:
            j = 0
            for elt in row.replace('\n', ''):
                board[170+i][170+j] = elt
                j += 1    
            i += 1


def new_char(l):
    l = ''.join(l).replace('.', '0').replace('#', '1')
    return algorithm[int(l, 2)]

def counting(board):
    count = 0
    for i in range(55, len(board) -55):
        count += board[i].count('#')
    return count

def solve(i,j, board):
    return new_char([board[i-1][j-1], board[i-1][j], board[i-1][j+1], board[i][j-1], board[i][j], board[i][j+1], board[i+1][j-1], board[i+1][j], board[i+1][j+1]])


# Part 1 & 2.
for k in range(50):
    new_board = init_board(size)
    for i in range(1, len(board) - 1):
        for j in range(1, len(board[i]) - 1):

            new_board[i][j] = solve(i, j, board)

    board = new_board.copy()
    if k == 1:
        print('Part 1:', counting(board))

print('Part 2:', counting(board))
