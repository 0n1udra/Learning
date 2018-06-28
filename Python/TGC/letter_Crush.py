def 1():
    # Code from The Great Courses, How to Program: Computer Science Concepts and Python Exercises, Lecture 13


    from random import choice

    def InitializeGrid(board):
        # Puts random letters in random places on board
        for i in range(8):
            for j in range(8):
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])

    # Starts the game
    def Initialize(board):
        # starts up the game
        InitializeGrid(board)
        # starts the score and turn variables
        global score
        score = 0
        global turn
        turn = 1

    # Continues game until objective complete
    def ContinueGame(current_score, goal_score = 100):
        if current_score <= goal_score:
            return True
        else:
            return False

    def DrawBoard(board):
        # Displays board
        linetodraw = ""
        # Prints blank lines
        print("\n\n\n")
        print("----------------------------------")
        # Draws rows from 8 down to 1
        for i  in range(7, -1, -1):
            # Draw each row
            linetodraw=str(i+1)
            for j in range(8):
                linetodraw += " | " + board[i][j]
            linetodraw += " |"
            print(linetodraw)
            print("----------------------------------")
        print("   a   b   c   d   e   f   g   h")
        print("Current Score: ", score)


    def GetMove():
        # Gets move form user
        move = input("Enter move > ")
        return move

    def Update(board, move):
        # Updates board form move
        SwapPieces(board, move)
        pieces_eliminated = True
        while pieces_eliminated:
            pieces_eliminated = RemovePieces(board)
            DropPieces(board)
            FillBlanks(board)

    def ConvertLetterToCol(Col):
        if Col == 'a':
            return 0
        elif Col == 'b':
            return 1
        elif Col == 'c':
            return 2
        elif Col == 'd':
            return 3
        elif Col == 'e':
            return 4
        elif Col == 'f':
            return 5
        elif Col == 'g':
            return 6
        elif Col == 'h':
            return 7
        else:
            # not valid column
            return -1
    # Do one rount of game
    def DoRound(board):
        # Runs one round of game
        # Displays board
        DrawBoard(board)
        # Get move
        move = GetMove()
        # update board
        Update(board, move)
        # Update turn number
        global turn
        turn += 1

    score = 0
    turn = 100
    goalscore = 100
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]


    def SwapPieces(board, move):
        # swap pieces on board according to move
        # gets original position
        origrow = int(move[1])-1
        origcol = ConvertLetterToCol(move[0])
        # get adjcent position
        if move[2] == 'u':
            newrow = origrow + 1
            newcol = origcol
        if move[2] == 'd':
            newrow = origrow - 1
            newcol = origcol
        if move[2] == 'l':
            newrow = origrow
            newcol = origcol - 1
        if move[2] == 'r':
            newrow = origrow
            newcol = origcol + 1

         # swap objects in two positions
        temp = board[origrow][origcol]
        board[origrow][origcol] = board[newrow][newcol]
        board[newcol][newcol] = temp

    def RemovePieces(board):
        # remove 3-in-a-row and 3-in-a-column pieces
        # Create board to store remove-or-not
        remove = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]

        # Go through rows
        for i in range(8):
            for j in range(6):
                if board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2]:
                    # three in a row are the same!
                    remove[i][j] = 1,
                    remove[i][j+1] = 1,
                    remove[i][j+2] = 1,

        # Go through columns
        for j in range(8):
            for i in range(6):
                if board[i][j] == board[i+1][j] and board[i+2][j] == board[i][j]:
                    # three in a column are the same!
                    remove[i][j] = 1,
                    remove[i+1][j] = 1,
                    remove[i+2][j] = 1,

        # Eliminate those marked
        global score
        removed_any = False
        for i in range(8):
            for j in range(8):
                if remove[i][j] == 1:
                    board[i][j] = 0
                    score += 1
                    removed_any = True
        return removed_any

        return False

    def DropPieces(board):
        # Drop pieces to fill in blanks
        for  j in range(8):
            # make list of pieces in column
            listofpieces = []
            for i in range(8):
                if board[i][j] != 0:
                    listofpieces.append(board[i][j])
            # copy that list into column
            for i in range(len(listofpieces)):
                board[i][j] = listofpieces[i]
            # fill in remainder of column with 0s
                for h in range(len(listofpieces), 0):
                    board[h][j] = 0



    def FillBlanks(board):
        # fill blanks with random pieces
        for i in range(8):
            for j in range(8):
                if board[i][j] == 0:
                    board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])


    # Starts
    Initialize(board)

    # Loops until said so
    while ContinueGame(score, goalscore):
        DoRound(board)

def 2():
# Initialize
# While game not over
# Do a round of the game
with Functions
    def Initialize():
# Initialize game
def ContinueGame():
# Return false if game should end, true if game is not over
def DoRound():

# Perform one round of the game
# Initialize game
Initialize()
# While game not over
while ContinueGame():
# Do a round of the game


def ContinueGame(current_score, goal_score=100):

# Return false if game should end, true if game is not over
if (current_score >= goal_score):
        return False
    else:
        return True

board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


def InitializeGrid(board):

# Initialize Grid by reading in from file
print("Initializing grid")

def Initialize(board):

# Initialize game
# Initialize grid
InitializeGrid(board)
# Initialize score
global score
score = 0
# Initialize turn number
global turn
turn = 1

# State main variables
score = 0
turn = 0
goalscore = 100
board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

from random import choice
def InitializeGrid(board):

# Initialize Grid by reading in from file
for i in range(8):
for j in range(8):
    board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])

    def DrawBoard(board):
# Display the board to the screen
print("Drawing Board")

def GetMove():

# Get the move from the user
print("Getting move")
return "b1u"

def Update(board, move):

# Update hte board according to move
print("Updating board")

def DoRound(board):

# Perform one round of the game
# Display current board
DrawBoard(board)
# Get move
move = GetMove()
# Update board
Update(board, move)
# Update turn number
global turn

def DrawBoard(board):

# Display the board to the screen
linetodraw = ""
# Draw some blank lines first
print("\n\n\n")
print(" ---------------------------------")
# Now draw rows from 8 down to 1
| 139
for i in range(7, -1, -1):
# Draw each row
linetodraw = ""
for j in range(8):
    linetodraw += " | " + board[i][j]
linetodraw += " |"
print(linetodraw)
print(" ---------------------------------")

string.

def GetMove():

# Get the move from the user
move = input("Enter move: ")
return move

with Functions
    def SwapPieces(board, move):
# Swap pieces on board according to move
print("Swapping Pieces")

def RemovePieces(board):

# Remove 3-in-a-row and 3-in-a-column pieces
print("Removing Pieces")
return False

def DropPieces(board):

# Drop pieces to fill in blanks
print("Dropping Pieces")

def FillBlanks(board):

# Fill blanks with random pieces
print("Filling Blanks")

def Update(board, move):

# Update the board according to move
SwapPieces(board, move)
pieces_eliminated = True
while pieces_eliminated:
    pieces_eliminated = RemovePieces(board)
DropPieces(board)
FillBlanks(board)



def ConvertLetterToCol(Col):
    if Col == 'a':
        return 0

elif Col == 'b':
return 1
elif Col == 'c':
return 2
elif Col == 'd':
return 3
elif Col == 'e':
return 4
elif Col == 'f':
return 5
elif Col == 'g':
return 6
elif Col == 'h':
return 7
else:
# not a valid column!
return -1

def SwapPieces(board, move):

# Swap pieces on board according to move
# Get original position
origrow = int(move[1]) - 1
origcol = ConvertLetterToCol(move[0])
# Get adjacent position
if move[2] == 'u':
    newrow = origrow + 1
newcol = origcol
elif move[2] == 'd':
newrow = origrow - 1
newcol = origcol
elif move[2] == 'l':
newrow = origrow
newcol = origcol - 1
elif move[2] == 'r':
newrow = origrow
newcol = origcol + 1
# Swap objects in two positions
temp = board[origrow][origcol]
board[origrow][origcol] = board[newrow][newcol]
board[newrow][newcol] = temp

    def RemovePieces(board):

    # Remove 3-in-a-row and 3-in-a-column pieces
    # Create board to store remove-or-not
    remove = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    # Go through rows
    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i][j + 1]) and (board[i][j] ==
                                                         board[i][j + 2]):
    # three in a row are the same!
    remove[i][j] = 1;
    remove[i][j + 1] = 1;
    remove[i][j + 2] = 1;
    # Go through columns
    | 143
    for j in range(8):
        for i in range(6):
            if (board[i][j] == board[i + 1][j]) and (board[i][j] ==
                                                         board[i + 2][j]):
    # three in a row are the same!
    remove[i][j] = 1;
    remove[i + 1][j] = 1;
    remove[i + 2][j] = 1;
    # Eliminate those marked
    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if remove[i][j] == 1
            board[i][j] = 0
    score += 1
    removed_any = True
    return removed_any


    def DropPieces(board):

    # Drop pieces to fill in blanks
    for j in range(8):
    # make list of pieces in the column
    listofpieces = []
    for i in range(8):
        if board[i][j] != 0:
            listofpieces.append(board[i][j])
    # copy that list into colulmn
    for i in range(len(listofpieces)):
        board[i][j] = listofpieces[i]
    # fill in remainder of column with 0s
    for i in range(len(listofpieces), 8):
        board[i][j] = 0


    def FillBlanks(board):

    # Fill blanks with random pieces
    for i in range(8):
        for j in range(8):
            if (board[i][j] == 0):
            board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])
    ͸ We finally have
