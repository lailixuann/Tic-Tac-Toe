import random
"""
CSC1024 Programming Principles: Final Project
A Computer Versus Human Tic-Tac-Toe Computer Game
"""


def display_data(board):
    """
    Function that display data in the board.
    """
    print("\n       |       |      ")
    print("   " + str(board[0][0]) +  "   |   " + str(board[0][1]) + "   |   " + str(board[0][2]) + "  ")
    print("_______|_______|_______")
    print("       |       |      ")
    print("   " + str(board[1][0]) +  "   |   " + str(board[1][1]) + "   |   " + str(board[1][2]) + "  ")
    print("_______|_______|_______")
    print("       |       |      ")
    print("   " + str(board[2][0]) +  "   |   " + str(board[2][1]) + "   |   " + str(board[2][2]) + "  ")
    print("       |       |      \n")


def user_input():
    """
    Function that ask user to input whether they want to start the game or not.
    """
    play = False
    while play == False:
        user = input("Do you wish to start the game? [y/n] : ") #ask for human input 
        if user.lower() == "y": 
            play = True #if lowercase of the input == "y", then play = True is returned
        elif user.lower() == "n":
            break #if lowercase of the input == "n", then it will break the loop and return play = False
        else:
            print("Wrong input, please try again!") #if lowercase of the input != "y" or "n", then it will print the message and continue the loop
    return play
 

def choose_mark():
    """
    Function that decide which mark go first in the game and ask user to choose their mark for the game.
    """
    computer_mark = ''
    human_mark = str(input("Please choose your mark [x/o]: ")) #ask for human input
    first_move = random.randint(0,1) #random number generator to see which mark go first in the game
    if first_move == 0: 
        first_move = 'x' #if it's 0, then 'x' will go first
        if human_mark == 'x': 
            computer_mark = 'o' #if human_mark == 'x', the computer mark = 'o'
            print("You chose 'x' and got the first move!") #then current message will be print
        elif human_mark == 'o':
            computer_mark = 'x' #if human_mark == 'o', the computer mark = 'x'
            print("You chose 'o' and Computer got the first move!") #then current message will be print
        else:
            choose_mark() #if human_mark != 'x' or 'o', it will call the function choose_mark() to get the human input again
    else: 
        first_move = 'o' # if it's 1, then 'o' will go first
        if human_mark == 'x':
            computer_mark = 'o' #if human_mark == 'x', the computer mark = 'o'
            print("You chose 'x' and Computer got the first move!") #then current message will be print
        elif human_mark == 'o':
            computer_mark = 'x' #if human_mark == 'o', the computer mark = 'x'
            print("You chose 'o' and got the first move!") #then current message will be print
        else:
            choose_mark()  #if human_mark != 'x' or 'o', it will call the function choose_mark() to get the human input again
    return first_move,human_mark,computer_mark #mark of first move, human_mark and computer_mark is returned


def isEmpty(board,row,column):
    """
    Function that check is the position of board empty.
    """
    empty = False 
    if board[row][column] == ' ': 
        empty = True #check if the position:(board[row][column]) in the board == ' ', then empty = True is returned
    return empty #if the position:(board[row][column]) in the board is occupied, then empty = False is returned


def isFull(board):
    """
    Function that check is the board full.
    """
    full = True
    for m in board:
        for n in m:
            if n == ' ':
                full = False #check if every column of every row of the board, if there is a position empty, then full = False will be returned
    return full #if every column of every row of the board is occupied, then full = True is returned
               

def human_move(board, mark):
    """
    Function that ask for human's move and place it into the board.
    """
    play = True
    while play == True: 
        row_input = int(input("Please enter the row you wish to place your mark: ")) #ask for human input
        column_input = int(input("Please enter the column you wish to place your mark: ")) #ask for human input
        if row_input in range(1,4) and column_input in range(1,4):
            row = row_input - 1
            column = column_input - 1 #if the input is in range(1,4) then row and column = input-1
            #it will continue to the next block of if-else statement
        else:
            print("Wrong input, please try again!")
            continue #if the input is not in range(1,4), current message will be printed and the loop will continue

        if isEmpty(board,row,column) == True:
            board[row][column] = mark #if the row and column human input in the board is empty, then mark will placed at the position
            play = False #play = False to stop the loop and
        elif isEmpty(board,row,column) == False:
            print("Sorry, this position is occupied!") #if the row and column human input in the board is empty, then current message will be printed
            #the loop will continue and ask for human input again
    return [row_input,column_input] #row_input and column_input of human input is return


def comp_move(board,mark):
    """
    Function that generate random move of computer and place its move into the board.
    """
    move = True
    while move == True:
        row = random.randint(0,2) #random number generates the row of computer move in range(0,2)
        column = random.randint(0,2) #random number generates the column of computer move in range(0,2)
        if isEmpty(board,row,column) == True: 
            board[row][column] = mark #if the position generated is empty in the board, then mark will placed at the position
            move = False #move = False then while loop break and return [row+1, column+1]
        elif isEmpty(board,row,column) == False:
            move = True #if the position generated is occupied in the board, then move=True and while loop continue
    return [row+1, column+1]
    

def isWinner(board,mark):
    """
    Function that checks is the mark a winner of the board.
    """
    win = False
    #if the three position in a row either vertical, horizontal of diagonal is the same and == mark
    if (board[0][0] == board[0][1] == board[0][2]  
        == mark) or (board[1][0] == board[1][1] == board[1][2] 
        == mark) or (board[2][0] == board[2][1] == board[2][2] 
        == mark) or (board[0][0] == board[1][0] == board[2][0] 
        == mark) or (board[0][1] == board[1][1] == board[2][1] 
        == mark) or (board[0][2] == board[1][2] == board[2][2] 
        == mark) or (board[0][0] == board[1][1] == board[2][2] 
        == mark) or (board[0][2] == board[1][1] == board[2][0] == mark):
        win = True #then win = True
        #if not, then win = False 
    return win 

    
def tieGame():
    """
    Function that print the message about the game is tie and has no winner.
    """
    print("The game is tie, no one wins!")


def game(board,first_move,human,computer):
    """
    Function of the game instruction.
    """
    move_count = 0 
    log = []
    if human == first_move: #human's mark == first_move mark
        while isFull(board) == False: #while the board is not full
            if isWinner(board,computer) == False: #if computer is not the winner
                h_move = human_move(board,human) #human_move is called
                move_count += 1 #move_count+1
                display_data(board) #display data of the board
                log.append([move_count,'H',h_move[0],h_move[1],'x']) #info will be append into log list
                #it will continue to the next block of if-else statement
            else: #if computer is the winner
                print("Sorry, computer won the game!") 
                break #print current message and break the loop

            if isFull(board) == False and isWinner(board,human) == False: #if human is not the winner and the board is not full
                c_move = comp_move(board,computer) #comp_move is called
                move_count += 1 #move_count+1
                display_data(board) #display data of the board
                log.append([move_count,'C',c_move[0],c_move[1],'o']) #info will be append into log list
                #while loop continue
            else: #if human is the winner
                print("Congratulations! You won the game!")   
                break #print current message and break the loop
        # while loop end when the board is full
            
        if isFull(board) == True and isWinner(board,computer) == False and isWinner(board,human) == False: 
            #if board is full, computer and human is not the winner
            tieGame() #function tieGame() is called
            
    elif computer == first_move: #if computer mark == first_move mark
        while isFull(board) == False: #while the board is not full
            if isWinner(board,human) == False: #if human is not the winner          
                c_move = comp_move(board,computer) #comp_move is called
                move_count += 1 #move_count+1
                display_data(board) #display data of the board
                log.append([move_count,'C',c_move[0],c_move[1],'o']) #info will be append into log list
                #it will continue to the next block of if-else statement
            else:
                print("Congratulations! You won the game!")
                break #print current message and break the loop

            if isFull(board) == False and isWinner(board,computer) == False: #if computer is not the winner and the board is not full
                h_move = human_move(board,human) #human_move is called
                move_count += 1 #move_count+1
                display_data(board) #display data of the board
                log.append([move_count,'H',h_move[0],h_move[1],'x']) #info will be append into log list
                #while loop continue
            else:
                print("Sorry, computer won the game!")
                break #print current message and break the loop
        # while loop end when the board is full
            
        if isFull(board) == True and isWinner(board,computer) == False and isWinner(board,human) == False:
            #if board is full, computer and human is not the winner
            tieGame() #function tieGame() is called
    return log #log list is return


def main():
    """
    Function of the Tic-Tac-Toe game.
    """
    print("Welcome to Tic Tac Toe!") #message printed
    start = user_input() # assign return value of user_input() to start
    with open ('logfile_22089148.txt','w') as openfile: #open file 'logfile_22089148.txt'
        while start == True: #while start return True 
            openfile.write('\n[MoveCount, (C/H), Row, Column, (o/x)]\n') #header of logfile
            board = [[' 'for x in range(3)] for x in range(3)] #assign an empty board to board
            first_move,human,computer = choose_mark() #choose_mark()
            display_data(board) #display data of the board
            log = (game(board,first_move,human,computer)) #assign return value of game(board,first_move,human,computer)to log
            start = user_input() #ask for user input and assign to start again to decide whether continue the while loop or not
            # if start = False, while loop end after executing the following codes
            for i in log:
                openfile.write(str(i) + '\n') #write each list in log list into lines of logfile
        print ("Byeee!") #print the message when while loop end
    return openfile 

main()

