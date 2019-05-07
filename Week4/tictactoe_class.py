class tictactoe():
    rows = 3
    cols = 3
    players = ["Player1", "Player2"]
    row_constraint = ["A", "B", "C"]
    col_constraint = [1, 2, 3]
    player_turn = 0
    draw = False

    def __init__(self):
        self.board = [["ㅁ" for col in range(self.cols)]for row in range(self.rows)]
    
    def is_draw(self):
        draw = 0
        for items in self.board:
            for item in items:
                if item != "ㅁ":
                    draw += 1
    
        if(draw == 9) and self.is_bingo() != -1:
            return True
        else:
            return False

    def is_bingo(self):
        #If player1 got bingo return 1 / if player2 got bingo reutrn 2, else return -1
        bingo = -1
        #가로 일치 여부
        for i in range(0, self.rows):
            if(self.board[i] == ["O", "O", "O"]):
                bingo = 1
            elif self.board[i] == ["X", "X", "X"]:
                bingo = 2
        
        #세로 일치 여부
        if(self.board[0][0] == self.board[1][0] == self.board[2][0] == "O"):
            bingo = 1
        elif(self.board[0][0] == self.board[1][0] == self.board[2][0] == "X"):
            bingo = 2

        if(self.board[0][1] == self.board[1][1] == self.board[2][1] == "O"):
            bingo = 1
        elif(self.board[0][1] == self.board[1][1] == self.board[2][1] == "X"):
            bingo = 2

        if(self.board[0][2] == self.board[1][2] == self.board[2][2] == "O"):
            bingo = 1
        elif(self.board[0][2] == self.board[1][2] == self.board[2][2] == "X"):
            bingo = 2

        #대각선 일치 여부
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] == "O"):
            bingo = 1
        elif(self.board[0][0] == self.board[1][1] == self.board[2][2] == "X"):
            bingo = 2
    
        if(self.board[2][0] == self.board[1][1] == self.board[2][0] == "O"):
            bingo = 1
        elif(self.board[2][0] == self.board[1][1] == self.board[2][0] == "X"):
            bingo = 2

        return bingo
    
    def put_in_position(self, position):
        #If False, the input is wrong or the sector is already occpied, so continue!
        i = position[0] #A, B or C
        j = int(position[1]) #1, 2 or 3
        
        if (i not in self.row_constraint) or (j not in self.col_constraint):
            print("The input is wrong...")
            return False
        
        #"A" 's ASCII Code is 65.
        i = int(ord(i)) - 65
        j = j-1

        if(self.board[i][j] != "ㅁ"):
            print("The sector is already occupied. Try again")
            return False
        
        if self.player_turn == 0:
            self.board[i][j] = "O"
        else:
            self.board[i][j] = "X"
        
        self.player_turn = 1 - self.player_turn
        return True
    
    def print_board(self):
        print("  1      2       3")
        for i in range(0, self.cols):
            print(chr(i+65), end = '')
            for j in range (0, self.rows):
                print(str(self.board[i][j]) + "\t", end = '')
            print("\n")
    
    def is_game_finished(self):
        if(self.is_draw()):
            print("Draw!")
            return True
        elif(self.is_bingo() == 1):
            print(self.players[0] + "wins!")
            return True
        elif(self.is_bingo() == 2):
            print(self.players[1] + "wins!")
            return True
        return False

game = tictactoe()

while not game.is_game_finished():
    print("===========================")
    game.print_board()
    print("===========================\n\n")

    position = input("Which row and column would you take, " + game.players[game.player_turn] + "? (ex. A3 for row 1 column 3): ")

    input_error = game.put_in_position(position)
    if(input_error == False):
        continue

print("End of the game.")