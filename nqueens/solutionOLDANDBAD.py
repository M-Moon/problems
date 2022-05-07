class Queen:
    def __init__(self, pos=[0,0]):
        self.position = pos

def gen_board():
    return [['-' for i in range(8)] for i in range(8)]

def populate_board(board, solution):
    for i in range(8):
        board[i][solution[i]] = 'q'
    return board

def print_board(board):
    for i in range(8):
        print(' '.join(board[i]))

def place_queen(board,x,y):
    board[x][y] = 'q'
    return board

###
# Checking/comparison functions
###

# Not actually needed, since a queen will definitely be on each row
# Therefore, is not used in the holistic checking function
def compare_x(q1, q2):
    if q1.position[0] == q2.position[0]:
        return False
    return True

def compare_y(q1, q2):
    if q1.position[1] == q2.position[1]:
        return False
    return True

def compare_diagonal(q1, q2):
    if abs(q1.position[0] - q2.position[0]) == abs(q1.position[1] - q2.position[1]):
        return False
    return True

# Evaluates whether two queens are seeing each other or not
def compare_queen_positions(q1, q2):
    if compare_y(q1,q2) and compare_diagonal(q1,q2): # compares queen positions without need to check row due to algorithm
        return False # They ARE NOT seeing each other
    return True # They ARE seeing each other

def trial_queen(t_queen, queen_list):
    for q in queen_list:
        if compare_queen_positions(t_queen, q):
            return False # unsuccessful
    return True

def generate_solution():
    board = gen_board()
    queen_list = list()
    compact_solution = list() # only stores column values

    for y in range(8): # row, y
        for x in range(8): # column, x
            t_queen = Queen([y,x]) # create trial queen
            if trial_queen(t_queen, queen_list): # check trial queen against already placed queens, and if true:
                queen_list.append(t_queen) # add accepted queen to list
                board[y][x] = 'q' # place queen on board for clarity
                compact_solution.append(x)
                break # stop checking this row

    return board

solution_board = generate_solution()
print_board(solution_board)
print()

##board = gen_board()
##board = place_queen(board, 1, 0)
##print_board(board)

bboard = gen_board()
bboard = populate_board(bboard, [0,1,2,3,4,5,6,7])
print_board(bboard)











