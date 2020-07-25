import poc_ttt_provided as provided
import random

NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

def mc_trial(board, player):
    """
    This function plays a game with the given board and the next player
    by making random moves
    """
    
    current_board = provided.TTTBoard(3, False, board)
    print current_board
    print current_board.check_win()
    
    while current_board.check_win() == None:
        
        empty_squares = current_board.get_empty_squares()
#        print empty_squares
    
        random_square = random.choice(empty_squares)
#        print random_square
    
        current_board.move(random_square[0], random_square[1], player)
        print current_board
        player = provided.switch_player(player)
        
    return current_board.clone()
    
#    Bunch of tests to check the accesibility

#    print provided.EMPTY, provided.PLAYERX,
#    print provided.PLAYERO, provided.DRAW
#    print provided.STRMAP[provided.EMPTY] == board[0][0]

#    print current_board
    
#    print current_board.square(0, 0)
#    print current_board.get_dim()
#    print current_board.get_empty_squares()
#    print current_board.clone()

    

current_player = 3
#my_board = [[random.choice(range(1, 4)) for num in range(3)] for num in range(3)] 

my_board = [[2, 1, 3],
            [1, 2, 1],
            [1, 1, 1]]

my_board = mc_trial(my_board, current_player)