"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    This function plays a game with the given board and the next player
    by making random moves
    """
    current_board = board
#    print current_board
#    print current_board.check_win()
    
    while current_board.check_win() == None:
        
        empty_squares = current_board.get_empty_squares()
#        print empty_squares
    
        random_square = random.choice(empty_squares)
#        print random_square
    
        current_board.move(random_square[0], random_square[1], player)
#        print current_board
        player = provided.switch_player(player)
    
#    if current_board.check_win() != provided.DRAW:
#        for row in range(3):
#            for col in range(3):
#                board[row][col] = current_board.square(row, col)
                
                
#    Bunch of tests to check the accesibility

#    print provided.EMPTY, provided.PLAYERX,
#    print provided.PLAYERO, provided.DRAW
#    print provided.STRMAP[provided.EMPTY] == board[0][0]

#    print current_board
    
#    print current_board.square(0, 0)
#    print current_board.get_dim()
#    print current_board.get_empty_squares()
#    print current_board.clone()

def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. 
    The function should find all of the empty squares with the maximum score
    and randomly return one of them as a (row, column) tuple
    """
    empty_squares = board.get_empty_squares()
    
#    print board
#    print scores
#    print empty_squares
    
    if len(empty_squares) > 1:
#        for dummy_num in range(200):
#            current_board = board.clone()
#            mc_trial(current_board, provided.PLAYERO)
#            mc_update_scores(score_board, current_board, provided.PLAYERO)

#        print my_board
#        print scores
#        print empty_squares
    
        max_value = -100
        for square in empty_squares:
            if scores[square[0]][square[1]] > max_value:
                max_value = scores[square[0]][square[1]]
            
#        print max_value
    
        best_move_grids = []
    
#        for row in range(board.get_dim()):
#            for col in range(board.get_dim()):
#                if scores[row][col] == max_value:
#                    best_move_grids.append((row, col))
        
        for square in empty_squares:
#            print square[0], square[1], max_value, scores[square[0]][square[1]]
            if scores[square[0]][square[1]] == max_value:
                best_move_grids.append(square)
                
#        print best_move_grids
        return random.choice(best_move_grids)
    else:
        return empty_squares[0]

def mc_update_scores(scores, board, player):
    """
    This function scores the grids with the appropriate value
    """
#    print board
#    print scores
#    print player
#    
#    print board.check_win()

    if board.check_win() == provided.PLAYERX:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == provided.PLAYERX:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == provided.PLAYERO:
                    scores[row][col] -= SCORE_CURRENT
    
    elif board.check_win() == provided.PLAYERO:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == provided.PLAYERO:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == provided.PLAYERX:
                    scores[row][col] -= SCORE_CURRENT
#    print scores

def mc_move(board, player, trials):
    """
    This function takes a current board, which player 
    the machine player is, and the number of trials to run. 
    The function returns a move for the machine player in 
    the form of a (row, column) tuple.
    """
    
    score_board = [[0 for dummy_num1 in range(board.get_dim())]
                   for dummy_num2 in range(board.get_dim())]
#    print board
#    print score_board
#    print
    
    for dummy_num in range(trials):
        current_board = board.clone()
        mc_trial(current_board, player)
        mc_update_scores(score_board, current_board, player)
#        print current_board
#        print score_board
        
#    print
#    print score_board
    return get_best_move(board, score_board)

#print mc_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.EMPTY], 
#                                           [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], 
#                                           [provided.PLAYERO, provided.EMPTY, provided.EMPTY]]), provided.PLAYERX, NTRIALS) 
#
#print mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
#                                     [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], 
#                                     [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO, NTRIALS)
#get_best_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.EMPTY], 
#                                           [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], 
#                                           [provided.PLAYERO, provided.EMPTY, provided.EMPTY]]), 
#              [[-3, 6, -2], 
#               [8, 0, -3], 
#               [3, -2, -4]])

#mc_update_scores([[0, 0, 0], 
#                  [0, 0, 0], 
#                  [0, 0, 0]], 
#                 provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
#                                              [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], 
#                                              [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]), 2) 
#
#mc_update_scores([[0, 0, 0], 
#                  [0, 0, 0], 
#                  [0, 0, 0]], 
#                 provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
#                                              [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO], 
#                                              [provided.EMPTY, provided.EMPTY, provided.PLAYERO]]), 2) 
#mc_update_scores([[0, 0, 0], 
#                  [0, 0, 0], 
#                  [0, 0, 0]], 
#                 provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
#                                              [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], 
#                                              [provided.PLAYERX, provided.PLAYERO, provided.PLAYERO]]), 2) 
#
#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
