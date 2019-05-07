import random

def put_in_position(pad, position, turn):
    i = int(position[0]) -1
    j = int(position[1]) -1
    if(pad[i][j] != "ㅁ"):
        print("Not Valid!")
        return pad
    if turn == 0:
        pad[i][j] = "O"
    else:
        pad[i][j] = "X"

    return pad

def is_row(pad):
    bingo = -1
    #알고리즘을 짜기엔 시간도 부족하고 생각이 너무 많아질 거 같아서 그냥 일단 포기.
    #행 일치 여부
    for i in range(0, 3):
        if(pad[i] == ["O", "O", "O"]):
            bingo = 0
        elif pad[i] == ["X", "X", "X"]:
            bingo = 1
    
    #열 일치 여부
    if(pad[0][0] == pad[1][0] == pad[2][0] == "O"):
        bingo = 0
    elif(pad[0][0] == pad[1][0] == pad[2][0] == "X"):
        bingo = 1

    if(pad[0][1] == pad[1][1] == pad[2][1] == "O"):
        bingo = 0
    elif(pad[0][1] == pad[1][1] == pad[2][1] == "X"):
        bingo = 1

    if(pad[0][2] == pad[1][2] == pad[2][2] == "O"):
        bingo = 0
    elif(pad[0][2] == pad[1][2] == pad[2][2] == "X"):
        bingo = 1

    #대각선 일치 여부
    if(pad[0][0] == pad[1][1] == pad[2][2] == "O"):
        bingo = 0
    elif(pad[0][0] == pad[1][1] == pad[2][2] == "X"):
        bingo = 1
    
    if(pad[2][0] == pad[1][1] == pad[2][0] == "O"):
        bingo = 0
    elif(pad[2][0] == pad[1][1] == pad[2][0] == "X"):
        bingo = 1

    return bingo

def print_pad(tictac):
    print("  1      2       3")
    for i in range(0, 3):
        print(str(i+1), end = '')
        for j in range (0, 3):
            print(str(pad[i][j]) + "\t", end = '')
        print("\n")

pad = [['ㅁ' for cols in range(3)]for rows in range(3)]
players = ["Player1", "Player2"]
current_player = 0
draw = 0

while(is_row(pad) == -1):
    print_pad(pad)
    position = input("Which row and column would you take, " + players[current_player] + "? (ex. 13 for row 1 column 3): ")
    
    put_in_position(pad, position, current_player)

    current_player = 1 - current_player

    for items in pad:
        for item in items:
            if item != "ㅁ":
                draw += 1
    
    if(draw == 9):
        break
    else:
        draw = 0


print_pad(pad)
if(is_row(pad) == 0):
    print(players[0] + " wins!")
elif(is_row(pad) == 1):
    print(players[1] + " wins!")
else:
    print("Draw!")

