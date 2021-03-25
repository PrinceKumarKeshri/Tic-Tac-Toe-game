# Tic-Tac-Toe-game

#Till now this is final code

from IPython.display import clear_output
import random

def display_board(board):
    
    clear_output()
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
    
def player_input():
    
    marker=''
    
    while not(marker == 'X' or marker=='O'):
        marker=input('Toss winner : \n\tDo you want to be X or O ?\n\t-------->>').upper()
    
    if marker =='X'and tosswinner=="player_1":
        return ('X','O')
    
    elif marker =='O'and tosswinner=="player_1":
        return ('O','X')
    
    elif marker =='X'and tosswinner=="player_2":
        return ('O','X')
    
    elif marker =='O'and tosswinner=="player_2":
        return ('X','O')
    
def place_marker(board,marker,position):
    board[position]=marker

    
def player_name():
    
    global pler_1, pler_2
    
    pler_1=input("Enter 1st player name : ")
    pler_2=input("Enter 2nd player name : ")
    
def win_check(board,mark):
    
    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or 
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or 
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))

def choose_first():
    
    clear_output()
    global tosswinner, player_2
    
    print("Toss: \n\tHead OR\tTail\n")
    player_1=input(f"{pler_1} select = ")
    
    if player_1.capitalize()=="Head":
        player_2='Tail'
        print(f"{pler_2} select = Tail")
    
    elif player_1.capitalize()=="Tail":
        player_2="Head"
        print(f"{pler_2} select = Head")
        
    
    input('press enter for continue : ')
    clear_output()
    
    h=0
    t=1
    ran=random.randint(0,1)
    
    if h == ran:
        
        print("\nToss Result : Head\n")
        
        if player_1.capitalize()=="Head":
            tosswinner='player_1'
            print(f"{pler_1} won the toss\n")
            
        elif player_2=="Head":
            tosswinner='player_2'
            print(f"{pler_2} won the toss\n")
        return "Head"
    
    elif t == ran:
        
        print("\nToss Result : Tail\n")
        
        if player_1.capitalize()=="Tail":
            tosswinner='player_1'
            print(f"{pler_1} won the toss\n")
            
        elif player_2=="Tail":
            tosswinner='player_2'
            print(f"{pler_2} won the toss\n")
        return 'Tail'
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

def replay():
    
    clear_output()
    return input('Do you want to play again? \n\tYes \n\tNo \n').lower().startswith('y')

print('Welcome to Tic Tac Toe!\n\n')

while True:

    theBoard = [' '] * 10
    name_of_players=player_name()
    toss_result = choose_first()
    turn = toss_result
    player1_marker, player2_marker = player_input()
    
    clear_output()
    
    print('\nDo you want to start the game ? \n\tYes \n\tNo\n')
    play_game = input("Enter your choice : ")
    if play_game.lower() == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
         
        if tosswinner=='player_1' and toss_result =='Head':
            
            if turn == "Head":

                display_board(theBoard)
                position = player1_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

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
                        turn = 'Tail'

            else:


                display_board(theBoard)
                position = player2_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print(f'\n\n{pler_2} has won!\n')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Head'
                        
                        
        
        elif tosswinner=='player_1' and toss_result =='Tail':
            
            if turn == "Tail":

                display_board(theBoard)
                position = player1_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

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
                        turn = 'Head'

            else:


                display_board(theBoard)
                position = player2_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print(f'\n\n{pler_2} has won!\n')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Tail'
                    
                    
                    
        elif tosswinner=='player_2' and toss_result=='Head':
            
            if turn == "Head":

                display_board(theBoard)
                position = player2_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print(f'\n\n{pler_2} have won the game!\n')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Tail'

            else:


                display_board(theBoard)
                position = player1_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print(f'\n\n{pler_1} has won!\n')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Head'
            
            
            
        elif tosswinner=='player_2' and toss_result=='Tail':
            
            if turn == "Tail":

                display_board(theBoard)
                position = player2_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print(f'\n\n{pler_2} have won the game!\n')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Head'

            else:


                display_board(theBoard)
                position = player1_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print(f'\n\n{pler_1} has won!\n')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Tail'
        
    input("press enter for continue .....")
        
    if not replay():
        break
