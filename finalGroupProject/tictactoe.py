import random

# Function to create a array to represent blank board.
def createBoard(board):
    board = [['_','_','_'],
             ['_','_','_'],
             ['_','_','_']]
    return board


# Function to print board
def boardPrinter(board):
    textStringPrep = ""
    for row in board:
        print(row)
        textStringPrep += str(row) + "\n" #remembers string form of board, use for scoreCard
    print('\n')
    return textStringPrep


# Take user input for location of X
def userTurn(board, row, column):
    if 0 < row < 4 and 0 < column < 4 and board[row - 1][column - 1] != 'X' and board[row - 1][column - 1] != 'O': #accounts for list index out of range
        board[row - 1][column - 1] = 'X'
    else:
        print("Invalid Location. Please pick between 1-3")
        # Reruns the entire function.
        row1 = input("Please enter a row \n")
        column1 = input("Please enter a column \n")
        userTurn(board, int(row1), int(column1))
    return board


# Take randomly generated number to pick a location for O
def computerTurn(board):
    while True:
        cpuRow = random.randint(0, 2)
        CPUColumn = random.randint(0, 2)
        if board[cpuRow][CPUColumn] != 'X' and board[cpuRow][CPUColumn] != 'O':
            board[cpuRow][CPUColumn] = 'O'
            break
            # Make function rerun if location is already filled
        else:
            continue
    return board

# Every turn, checks each row, column, and diagonal to see if either player has won or tied
def winCheck(board):
    # row check
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]=='X':
            print("You win!")
            return 1
        elif board[i][0]==board[i][1]==board[i][2]=='O':
            print("The computer wins!")
            return 2
    # column check
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]=='X':
            print("You win!")
            return 1
        elif board[0][i]==board[1][i]==board[2][i]=='O':
            print("The computer wins!")
            return 2
        
     # diagonal check
    if board[0][2]==board[1][1]==board[2][0] == 'X': #forward slash player
        print("You win!")
        return 1
    elif board[0][2]==board[1][1]==board[2][0] == 'O': #forward slash computer
        print("The computer wins!")
        return 2
    elif board[0][0]==board[1][1]==board[2][2] == 'X': #back slash player
        print("You win!")
        return 1
    elif board[0][0]==board[1][1]==board[2][2] == 'O': #back slash computer
        print("The computer wins!")
        return 2

    #tie game check
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board [r][c] == '_':
                return 0
            
    #No win conditions triggered, no empty spaces, Tie Game
    print("Tie Game")
    return 3

# ask the user if they want to play again
def playAgain():
    reply = input('Do you want to play again?(yes, no): \n')
    reply = reply.lower()
    if reply == 'yes':
        ticTacToe()
    else:
        print("The game is over.")

# writes game results to textfile
def scoreCard(printableBoard, state): # takes in printableBoard string, not actual board
    handle = open("ticTacToeResults.txt", "w")
    handle.write(printableBoard)
    handle.write("\n")
    if state == 1:
        handle.write("You win!")
    elif state == 2:
        handle.write("The computer wins!")
    elif state == 3:
        handle.write("Tie game")

    handle.close()
        
        
# main function
def ticTacToe():
    test = []
    test = createBoard(test)

    while True:
        print("Computer turn. ")
        test = computerTurn(test)

        printableBoard = boardPrinter(test)
        state = winCheck(test)
        if state == 1 or state == 2 or state == 3:
            scoreCard(printableBoard, state)
            playAgain()
            break
      
        print("Player turn. ")
        row = input("Please enter a row \n")
        column = input("Please enter a column \n")
        userTurn(test, int(row), int(column))
        printableBoard = boardPrinter(test)
        state = winCheck(test)
        if state == 1 or state == 2 or state == 3:
            scoreCard(printableBoard, state)
            playAgain()
            break

  
ticTacToe()

'''
    Computer turn.
    ['O', '_', '_']
    ['_', '_', '_']
    ['_', '_', '_']


    Player turn.
    Please enter a row
    3
    Please enter a column
    3
    ['O', '_', '_']
    ['_', '_', '_']
    ['_', '_', 'X']


    Computer turn.
    ['O', '_', '_']
    ['_', '_', 'O']
    ['_', '_', 'X']


    Player turn.
    Please enter a row
    1
    Please enter a column
    3
    ['O', '_', 'X']
    ['_', '_', 'O']
    ['_', '_', 'X']


    Computer turn.
    ['O', '_', 'X']
    ['_', '_', 'O']
    ['_', 'O', 'X']


    Player turn.
    Please enter a row
    3
    Please enter a column
    1
    ['O', '_', 'X']
    ['_', '_', 'O']
    ['X', 'O', 'X']


    Computer turn.
    ['O', 'O', 'X']
    ['_', '_', 'O']
    ['X', 'O', 'X']


    Player turn.
    Please enter a row
    2
    Please enter a column
    2
    ['O', 'O', 'X']
    ['_', 'X', 'O']
    ['X', 'O', 'X']


    You win!
    Do you want to play again?(yes, no):
    yes
    Computer turn.
    ['_', '_', '_']
    ['_', '_', 'O']
    ['_', '_', '_']


    Player turn.
    Please enter a row
    1
    Please enter a column
    1
    ['X', '_', '_']
    ['_', '_', 'O']
    ['_', '_', '_']


    Computer turn.
    ['X', 'O', '_']
    ['_', '_', 'O']
    ['_', '_', '_']


    Player turn.
    Please enter a row
    2
    Please enter a column
    1
    ['X', 'O', '_']
    ['X', '_', 'O']
    ['_', '_', '_']


    Computer turn.
    ['X', 'O', '_']
    ['X', '_', 'O']
    ['O', '_', '_']


    Player turn.
    Please enter a row
    3
    Please enter a column
    3
    ['X', 'O', '_']
    ['X', '_', 'O']
    ['O', '_', 'X']


    Computer turn.
    ['X', 'O', 'O']
    ['X', '_', 'O']
    ['O', '_', 'X']


    Player turn.
    Please enter a row
    3
    Please enter a column
    2
    ['X', 'O', 'O']
    ['X', '_', 'O']
    ['O', 'X', 'X']


    Computer turn.
    ['X', 'O', 'O']
    ['X', 'O', 'O']
    ['O', 'X', 'X']


    The computer wins!
    Do you want to play again?(yes, no):
    yes
    Computer turn.
    ['_', '_', '_']
    ['_', '_', '_']
    ['_', '_', 'O']


    Player turn.
    Please enter a row
    3
    Please enter a column
    2
    ['_', '_', '_']
    ['_', '_', '_']
    ['_', 'X', 'O']


    Computer turn.
    ['O', '_', '_']
    ['_', '_', '_']
    ['_', 'X', 'O']


    Player turn.
    Please enter a row
    2
    Please enter a column
    2
    ['O', '_', '_']
    ['_', 'X', '_']
    ['_', 'X', 'O']


    Computer turn.
    ['O', '_', '_']
    ['_', 'X', '_']
    ['O', 'X', 'O']


    Player turn.
    Please enter a row
    2
    Please enter a column
    1
    ['O', '_', '_']
    ['X', 'X', '_']
    ['O', 'X', 'O']


    Computer turn.
    ['O', '_', 'O']
    ['X', 'X', '_']
    ['O', 'X', 'O']


    Player turn.
    Please enter a row
    3
    Please enter a column
    2
    Invalid Location. Please pick between 1-3
    Please enter a row
    2
    Please enter a column
    3
    ['O', '_', 'O']
    ['X', 'X', 'X']
    ['O', 'X', 'O']


    You win!
    Do you want to play again?(yes, no):
    no
    The game is over.
'''
