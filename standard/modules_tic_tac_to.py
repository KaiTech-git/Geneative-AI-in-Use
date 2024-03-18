def choose_symbol():
    result=''
    while result.upper() not in ["X","O"]:
        result = input("Do you want to play with X or O")
        if result.upper() in ["X","O"]:
            return result.upper()
        else:
            print("I don't understand.")

def  board_index_print():
    board_net={"A": " 1 | 2 | 3 ", "B":"---|---|---", "C": " 4 | 5 | 6 ",
             "D":"---|---|---", "E": " 7 | 8 | 9 " }
    for val in board_net.values():
        print(val)
    return

def choose_position(board,dic_players,player):
    result = ""
    p_empty = False
    while (result not in range(1,10)) or not p_empty:
        result=input("{player}>>Enter your move(1-9):".format(player = player))
        
        if not result.isdigit():
            print("Try again!")
        elif int(result) in range(1,10) and board[result] not in ["X","O"]:
            p_empty =True
            return result
        else:
            print("Try again!")

def show_board(board):
    board_net={"A": " 1 | 2 | 3 ", "B":"---|---|---", "C": " 4 | 5 | 6 ",
             "D":"---|---|---", "E": " 7 | 8 | 9 " }
    for a,b in board_net.items():
        for k,l in board.items():
            if str(k )in b:
                b=b.replace(k,l)
        print(b)
    return 

def evaluate(board,dic_players,player):
    evaluate_vector =[[1,2,3], [4,5,6], [7,8,9],
                    [1,4,7], [2,5,8], [3,6,9],
                    [1,5,9], [3,5,7]]
    if " " not in board.values():
        print("Draw thanks for playing!")
        return False
    for vector in evaluate_vector:
        count=0
        for element in vector:
            if board[str(element)]==dic_players[player]:
                count+=1
        if count ==3:
            print(f'{player}>> Wins the game!')
            return False
    return True

def next_game():
    result=''
    while result.upper() not in ["Y","N"]:
        result = input("Do you want to play new game Y/N")
        if result.upper() in ["Y","N"]:
            return result.upper()=="Y"
        else:
            print("I don't understand.")

if __name__ == "__main__":
    pass