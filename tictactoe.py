import time 

tictactoe_board = {
"Top-L":" ","Top-M":" ","Top-R":" ",
"Mid-L":" ","Mid-M":" ","Mid-R":" ",
"Bot-L":" ","Bot-M":" ","Bot-R":" "
}



def printBoard(Board):
    print(Board["Top-L"]+" |"+Board["Top-M"]+" |"+Board["Top-R"])
    print(" -+--+-")
    print(Board["Mid-L"]+" |"+Board["Mid-M"]+" |"+Board["Mid-R"])
    print(" -+--+-")
    print(Board["Bot-L"]+" |"+Board["Bot-M"]+" |"+Board["Bot-R"])

Draw = 0

def maingame():
    count = 0
    global turn
    turn = "X"
    print("Hello and welcome to Tic-Tac-Toe!")
    time.sleep(2)
    while count < 10:
        printBoard(tictactoe_board)
        time.sleep(1)
        print("It is " + turn + "'s turn.")
        time.sleep(1)
        move = input("Where do you want to play?\n")
        time.sleep(1)
        while move not in tictactoe_board.keys() or tictactoe_board[move] == "X" or tictactoe_board[move] == "O":
            move = input("Please enter a valid place: ")
        tictactoe_board[move] = turn
        count += 1
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        if count >= 5:
            if tictactoe_board["Top-L"] == tictactoe_board["Top-M"] == tictactoe_board["Top-R"]:
                break
            elif tictactoe_board["Mid-L"] == tictactoe_board["Mid-M"] == tictactoe_board["Mid-R"]:
                break
            elif tictactoe_board["Bot-L"] == tictactoe_board["Bot-M"] == tictactoe_board["Bot-R"]:
                break
            elif tictactoe_board["Top-L"] == tictactoe_board["Mid-L"] == tictactoe_board["Bot-L"]:
                break
            elif tictactoe_board["Top-M"] == tictactoe_board["Mid-M"] == tictactoe_board["Bot-M"]:
                break
            elif tictactoe_board["Top-R"] == tictactoe_board["Mid-R"] == tictactoe_board["Bot-R"]:
                break
            elif tictactoe_board["Top-R"] == tictactoe_board["Mid-M"] == tictactoe_board["Bot-L"]:
                break 
            elif tictactoe_board["Top-L"] == tictactoe_board["Mid-M"] == tictactoe_board["Bot-R"]:
                break 
            elif count == 9:
                printBoard(tictactoe_board)
                print("It is a draw!")
                playagain = input("Do you want to play again?(Y/N): ").lower()

                if playagain == "y":
                    for k in tictactoe_board.keys():
                        tictactoe_board[k] = " "
                    maingame()
                else:
                    exit()


                
    printBoard(tictactoe_board)
    if turn == "X":
        turn = "O"
    else:
        turn = "X"   
   
    
    print("Congratulations! " + turn + " Won.")
    playagain = input("Do you want to play again?(Y/N): ").lower()

    if playagain == "y":
        for k in tictactoe_board.keys():
            tictactoe_board[k] = " "
        maingame()
    else:
        exit()


if __name__ == "__main__":
    maingame()
        
            







    


    
    


