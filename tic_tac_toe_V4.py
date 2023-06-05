
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 01:28:36 2023

@author: 0526p
"""

#Till now this is final code



def display_number():
    print('Follow these number:')
    print("7|8|9")
    print("- - -")
    print("4|5|6")
    print("- - -")
    print("1|2|3")

def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def place_marker(board,marker,position):
    board[position]=marker
 
def player_name():
    
    global pler_1, pler_2
    pler_1=input("Enter 1st player name : ")    
    pler_2=input("Enter 2nd player name : ")
    
def player_input():
    
    marker=''
    while not(marker == 'X' or marker=='O'):
        marker=input(f'{pler_1.capitalize()} choose one of the option X or O ?\n\t-------->>').upper()
    if marker =='X':
        print(f"{pler_1.capitalize()} choosed option: 'X'")
        print(f"{pler_2.capitalize()} choosed option: 'O'")
        return ('X','O')    
    elif marker =='O':
        print(f"{pler_1.capitalize()} choosed option: 'O'")
        print(f"{pler_2.capitalize()} choosed option: 'X'")
        return ('O','X')

def win_check(board,mark):
    
    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or 
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or 
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player1_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'{pler_1} choose your position between 1 to 9 = '))
    return position

def player2_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'{pler_2} choose your position between 1 to 9 = '))        
    return position

def reply():
    replay_option=''
    
    while not(replay_option == 'PLAY AGAIN' or replay_option=='NEW GAME' or replay_option== 'EXIT'):
        replay_option=input('Choose one of the option ?\n\tPlay Again \n\tNew Game \n\tExit \n\t-------->>').upper()
    
    return replay_option

def play_again(name_of_players):
    
    player1_marker, player2_marker = player_input()
    return player1_marker, player2_marker
    
def play(theBoard, game_on, player1_marker, player2_marker):
    num = 0
    while game_on:
        
        if num %2 == 0:
            display_board(theBoard)
            position = player1_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            num = num + 1
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print(f'\n\n{pler_1} have won the game!\n')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
            
        else:
            display_board(theBoard)
            position = player2_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            num = num + 1
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print(f'\n\n{pler_2} have won the game!\n')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break

print('Welcome to Tic Tac Toe!\n\n')
display_number()

while True:

    theBoard = [' '] * 10
    name_of_players=player_name()
    
    player1_marker, player2_marker=play_again(name_of_players)         
    
    play_game = ''
    while not(play_game == 'YES' or play_game=='NO' or play_game=='EXIT'):
        play_game=input('\nDo you want to start the game ?\n\tYes \n\tNo \n\tExit \n\t-------->>').upper()
    if play_game.lower() == 'yes':
        game_on = True
    elif play_game.lower() == 'no':
        continue    
    elif play_game.lower() == 'exit':
        break
    play(theBoard, game_on, player1_marker, player2_marker)
    
    input("press enter for continue .....")    
    exi = ''
    
    while True:
        reply_option = reply()
        if reply_option == 'PLAY AGAIN':
            theBoard = [' ']*10
            
            player1_marker, player2_marker=play_again(name_of_players)         
        
            play_game = ''
            while not(play_game == 'YES' or play_game=='NO' or play_game=='EXIT'):
                play_game=input('\nDo you want to start the game ?\n\tYes \n\tNo \n\tExit \n\t-------->>').upper()
            
            if play_game.lower() == 'yes':
                game_on = True
            elif play_game.lower() == 'no':
                continue    
            elif play_game.lower() == 'exit':
                exi = 'EXIT'
                break
            play(theBoard, game_on, player1_marker, player2_marker)
            
            input("press enter for continue .....")
        elif reply_option == 'NEW GAME':
            break
        elif reply_option == 'EXIT':
            exi = 'EXIT'
            break
        
    if exi == 'EXIT':
        break
    else:
        pass
        
   
    
    

                
print('Thank You')
