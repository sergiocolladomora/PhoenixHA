import random

def display_board(board):
    '''Displays the current state of the board.'''
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def win_check(board):
    '''Checks if there is a win on the board.'''
    return ((board[1] == board[2] == board[3] != ' ') or
            (board[4] == board[5] == board[6] != ' ') or
            (board[7] == board[8] == board[9] != ' ') or
            (board[1] == board[4] == board[7] != ' ') or
            (board[2] == board[5] == board[8] != ' ') or
            (board[3] == board[6] == board[9] != ' ') or
            (board[1] == board[5] == board[9] != ' ') or
            (board[3] == board[5] == board[7] != ' '))

def full_board_check(board):
    '''Checks if the board is full.'''
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True

def mark_position(board, player):
    '''Marks the board at the position chosen by the player.'''
    while True:
        try:
            # Add try/except block here:
            position = int(input(player + ', choose your next position (1-9): '))
        except ValueError:
            print("Invalid input.") # Handles non-numeric input (like "hello")
            continue # Goes back to the start of the while True loop
        if 1 <= position <= 9 and board[position] == ' ':
            if player == 'Player 1': 
                board[position] = 'X'
            else:
                board[position] = 'O'
            return board
        else:
            print("Invalid position.")

def replay():
    '''Asks the players if they want to play again.'''
    while True:
        choice = input('Do you want to play again? (y/n) ')

        if choice.lower().startswith('y'):
            print("Starting a new game...")
            return True
            break

        elif choice.lower().startswith('n'):
            print("Thanks for playing! Exiting game.")
            return False
            break
            
        else:
            print("Invalid input.")

def main():
    '''Main function to run the Tic-Tac-Toe game.'''
    #Intro to the game
    print("Welcome to Tic Tac Toe! \n Player 1 is 'X' and Player 2 is 'O'. \n Each player must enter the number of the position of the following board: \n 123\n 456\n 789")
    play=True

    while play:
        #Set up the board
        the_board = [' ']*10
        turn = 'Player 1'
        print(turn + ' will go first!')

        game_on = True

        while game_on:
            display_board(the_board)
            the_board= mark_position(the_board, turn)

            if win_check(the_board):
                display_board(the_board)
                print('Congratulations! ' + turn + ' has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    if(turn == 'Player 1'):
                        turn = 'Player 2'
                    else:
                        turn = 'Player 1'


        play = replay()

if __name__ == "__main__":
    main()


