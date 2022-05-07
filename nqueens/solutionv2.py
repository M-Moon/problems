# N-Queens Problem
# Recursive algorithm to find every solution to placing N-Queens on an N-Queen size chessboard without any Queen seeing another

NUM_QUEENS = 8 # 8 default

solution = [0 for x in range(NUM_QUEENS)]
solution_bank = list()

def check_pos(test_row, test_column):
    # Row 0 will have no other queens placed, so can be skipped
    if test_row == 0:
        return True

    for r in range(test_row):
        # Checking vertical
        if test_column == solution[r]: # checking if tested column is equal to the currently checked row's column
            return False

        # Checking diagonal
        if abs(test_row - r) == abs(test_column - solution[r]): # neat way of testing for seeing if two queens are on the same diagonal
            return False

    # Position is safe
    return True

def gen_solutions(row=0):
    global solution, solution_bank, NUM_QUEENS # must be global to read the variables recursively I guess. forgot this and it caused me so much grief
    
    for queen_column in range(NUM_QUEENS): # checking through every valid column with the current solution setup
        if not check_pos(row, queen_column):
            continue
        else:
            solution[row] = queen_column # usable column found, put it into the current solution
            gen_solutions(row+1) # recurse

    if row == NUM_QUEENS: # base case / end condition
        solution_bank.append(solution.copy()) # add current found solution, go back up to check other variations
        return

print()
gen_solutions()
#print(solution)
#print(solution_bank)
print("There have been {} solutions found!".format(len(solution_bank)))
print()

###
# Use below code to get simple text-based visualisation of a chosen solution from the solution bank :)
###

def gen_board():
    return [['-' for i in range(NUM_QUEENS)] for i in range(NUM_QUEENS)]

def populate_board(board, solution):
    for i in range(NUM_QUEENS):
        board[i][solution[i]] = 'q'
    return board

def print_board(board):
    for i in range(NUM_QUEENS):
        print(' '.join(board[i]))

board = gen_board()
board = populate_board(board, solution_bank[-1]) # use solution_bank index to choose a solution to look at
print_board(board)
        
        
