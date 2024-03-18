from dotenv import load_dotenv
from openai import OpenAI
import os
import re

load_dotenv()

#client = OpenAI(os.getenv('OPENAI_API_KEY'))

def initialize_chatGPT(symbol,client):
    
    context = [{'role':'system', 'content':f"""You are a bot playing Tic Tac To game with human opponent.\
               You goal is to get 3 {symbol} symbols in one line on a board before your opponent.\
               game board looks like this where numbers correspond to positions on the board:\
                1 | 2 | 3 \
                4 | 5 | 6 \
                7 | 8 | 9\
                During every turn you will get positions of all symbols on a board in for of dictionary.\
                Here is an example:\
                {{"1": " ","2":"X","3":"O", "4":"X","5":" ","6":" ", "7":" ", "8":" ", "9":" "}}\
                Based on the data in dictionary provide you will provide your move.\
                Your move should be a number from 1 to 9 expressed in following form:\
                <<5>>\
                Try to make the game difficult for your opponent."""}]
    get_completion_from_messages(client, context)
    return context

def get_completion_from_messages (client, messages,model="gpt-3.5-turbo", temperature=0,):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

def GPT_turn(context:list, board:dict , client):
    message ={'role':'user', 'content': f"""Board looks like this after last move: 
              {board}
              What is your move?"""}
    
    context.append(message)
    response = get_completion_from_messages(client,context)
    context.append({'role':'assistant', 'content': response})
    
    p_empty = False
    match = re.search(r'<<(\d+)>>', response)

    while ( match.group(1) not in range(1,10)) or not p_empty:
        match = re.search(r'<<(\d+)>>', response)
        result = int(match.group(1))
            
        if not match:
            message ={'role':'user', 'content': f"""There was no specific position in your reply.
                      Please try again and format your response like this example: "<<6>>".
                      What is your move?"""}
            context.append(message)
            response = get_completion_from_messages(client, context)
            
            context.append({'role':'assistant', 'content': response})
        elif int(result) in range(1,10) and board[str(result)] not in ["X","O"]:
                p_empty =True
                return str(result), context
        else:
            message ={'role':'user', 'content': f"""This position is occupied pleas try again."""}
            context.append(message)
            response = get_completion_from_messages(client, context)
    
    
    
    