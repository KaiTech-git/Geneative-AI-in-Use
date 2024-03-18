from os import system
from standard.modules_tic_tac_to import choose_symbol, board_index_print, choose_position, show_board, next_game, evaluate


if __name__ == "__main__":
    game_on=True
    d={"player1": "O", "player2": "X"}
    board={"1": " ","2":" ","3":" ", "4":" ","5":" ","6":" ", "7":" ", "8":" ", "9":" "}

    while game_on:
        board={"1": " ","2":" ","3":" ", "4":" ","5":" ","6":" ", "7":" ", "8":" ", "9":" "} 
        print('Welcome to Tic Tac Toe game!')
        d["player1"]= choose_symbol()
        if d["player1"]=="X":
            d["player2"]="O"
        else:
            d["player2"]="X"

        player="player1"
        board_index_print()
        
        while game_on:
            board[choose_position(board,d,player)]= d[player]
            
            show_board(board)
            
            game_on=evaluate(board,d,player)


            if game_on == False:
                game_on =next_game()
                if game_on==True:
                    system('clear')
                    break
            
            if player == "player1":
                player= "player2"
            else:
                player= "player1"