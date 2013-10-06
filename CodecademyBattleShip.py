import random

board = list()
board.append(["O"]*5)
#print board

for el in range(1,len(board[0])):
    board.append(["O"]*5)
    
    
#print board

		


def print_board(board):
    for el in board:
	print ' '.join(el)
	


def random_row(board):
    rowLen = len(board)
    return random.randint(0,rowLen -1)

#print random_row(board)

def random_col(board):
    colLen = len(board)
    return random.randint(0,colLen -1)

#print random_col(board)
ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    try:
	guess_row = input("Guess Row:")
	guess_col = input("Guess Col:")
    except:
	print "Enter good number!"
	continue
    
    if guess_row == ship_row and guess_col == ship_col:
	print "Congratulations! You sunk my battleship!"
	break
    else:
	if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
	    print "Oops, that's not even in the ocean."
	elif(board[guess_row][guess_col] == "X"):
	    print "You guessed that one already."
	else:
	    print "You missed my battleship!"
	    board[guess_row][guess_col] = "X"
	    print turn + 1	
        print_board(board)
	if turn == 3:
	    print "Game Over"	




#print_board_pretty(board)
