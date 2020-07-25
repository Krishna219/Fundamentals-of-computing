"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided
#import user43_SJVRDb3Yxc_1 as provided
#import user43_H1ZYZcRdPY_14 as poc_format_testsuite

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

#turn ON print statements
DEBUG = 0

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    
    
    winner = board.check_win()
    
    empty_squares = board.get_empty_squares()
    
    if DEBUG:
        print "-"*20
        print board
        print "Winner : ", winner
        print "Possible moves : ",empty_squares
    
    
    #base case check winner and return valid score and move
    if winner:
        return SCORES[winner], (-1, -1)
    
    #recursive case check valid moves
    
    
    score, move = 0, (0, 0)
    
    #list of scores of all possible board moves
    score_list = []
    move_list = []
    
    #for every valid move make move and call minimax for opposite player 
    for square in empty_squares:
        
        #copy board
        child_board = board.clone()
        
        #make move
        child_board.move(square[0], square[1], player) 
        
        #call minimax for every valid move
        child_score = mm_move(child_board, provided.switch_player(player)) 
        
        if DEBUG:
            print "-"*20
            print "Board score for move of player :", player, "at position :", square
            print child_board
            print "Score : ", child_score[0], "Move : ", square
        
        score_list.append(child_score[0])
        move_list.append(square)
        
#        #quit the loop when you find winning move for player
#        if player == provided.PLAYERX and child_score[0] == 1:
#            break
#        elif player == provided.PLAYERX and child_score[0] == -1:
#            break
        
    if DEBUG:
        print 
    
    #maximize for player x and minimize for player o
    if player == provided.PLAYERX:
        score = max(score_list)
        move = move_list[score_list.index(score)]
    elif player == provided.PLAYERO:
        score = min(score_list)
        move = move_list[score_list.index(score)]
        
#        #maximize for player x and minimize for player o
#        if player == provided.PLAYERX:
#            score, move = (score, move) if score > child_score[0] else (child_score[0], square)
#            if score == 1:
#                return score, move
#        elif player == provided.PLAYERO:
#            score, move = (score, move) if score < child_score[0] else (child_score[0], square)
#            if score == -1:
#                return score, move
            
    return score, move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

# run the testing suite for our format function
#poc_format_testsuite.run_suite(mm_move)
#X = provided.PLAYERX
#O = provided.PLAYERO
#_ = provided.EMPTY
#    
#J = [[O, X, X], [O, X, _], [X, O ,X]] #Test #10
#
#print mm_move(provided.TTTBoard(3, False, J), provided.PLAYERX)
print mm_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], 
                                           [provided.EMPTY, provided.EMPTY]]), provided.PLAYERX)