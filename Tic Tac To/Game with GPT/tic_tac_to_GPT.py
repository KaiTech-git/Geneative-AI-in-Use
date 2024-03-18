from openai import OpenAI
from os import system, getenv
from modules_standard import choose_symbol, board_index_print, show_board, next_game, evaluate, choose_position
from GPT_module import initialize_chatGPT, GPT_turn


if __name__ == "__main__":
    game_on=True
    d={"player1": "O", "playerGPT": "X"}
    board={"1": " ","2":" ","3":" ", "4":" ","5":" ","6":" ", "7":" ", "8":" ", "9":" "}
    global client
    client = OpenAI(api_key=getenv('OPENAI_API_KEY'))

    while game_on:
        board={"1": " ","2":" ","3":" ", "4":" ","5":" ","6":" ", "7":" ", "8":" ", "9":" "} 
        print('Welcome to Tic Tac Toe game!')
        d["player1"]= choose_symbol()
        if d["player1"]=="X":
            d["playerGPT"]="O"
        else:
            d["playerGPT"]="X"

        context = initialize_chatGPT(d["playerGPT"], client)
        
        player="player1"
        board_index_print()
        
        while game_on:
            if player == "player1":
                board[choose_position(board,player)]= d[player]
            else:
                move, context = GPT_turn(context, board, client)
                board[move]= d[player] #GPT
            
            show_board(board)
            
            game_on=evaluate(board,d,player)


            if game_on == False:
                game_on =next_game()
                if game_on==True:
                    system('clear')
                    break
            
            if player == "player1":
                player= "playerGPT"
            else:
                player= "player1"