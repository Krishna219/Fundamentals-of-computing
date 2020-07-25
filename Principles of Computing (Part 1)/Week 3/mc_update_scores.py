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
    current_board = board
    print current_board
#    print current_board.check_win()
    
    while current_board.check_win() == None:
        
        empty_squares = current_board.get_empty_squares()
#        print empty_squares
    
        random_square = random.choice(empty_squares)
#        print random_square
    
        current_board.move(random_square[0], random_square[1], player)
        print current_board
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

def get_squares(board, player):
    """
    This is an helper function takes the played board and the player and
    returns the list of square indexes (row, col) in which the player 
    has played
    """
#    print board
#    print player
    grids = []
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if board.square(row, col) == player:
                grids.append((row, col))
    
    return grids

def update_score(scores, grids, value):
    """
    This function scores the grids with the appropriate value
    """
#    print scores
#    print grids
#    print value

    for grid in grids:
        scores[grid[0]][grid[1]] += value
    
    print scores
    
def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) 
    with the same dimensions as the Tic-Tac-Toe board, 
    a board from a completed game, and which player the machine player is.
    The function should score the completed board and update the scores
    grid. As the function updates the scores grid directly, 
    it does not return anything
    """
#    print board
#    print scores
    
    player_grids = get_squares(board, player)
    other_grids = get_squares(board, provided.switch_player(player))
    
    if board.check_win() == player:
#        print player_grids
        
        update_score(scores, player_grids, SCORE_CURRENT)
        update_score(scores, other_grids, - SCORE_OTHER)
        
    elif board.check_win() == provided.switch_player(player):
#        print other_grids
        
        update_score(scores, other_grids, SCORE_OTHER)
        update_score(scores, player_grids, - SCORE_CURRENT)


        
#    print provided.STRMAP[player]    
#    print provided.STRMAP[board.check_win()]
#    print provided.switch_player(player)
    
#    if board.check_win() == player:
#        for row in range(board.get_dim()):
#            for col in range(board.get_dim()):
#                if board.square(row, col) == player:
#                    print (row, col)
#                    scores[row][col] += 
#                    
#    elif board.check_win() == provided.switch_player(player):
#        for row in range(board.get_dim()):
#            for col in range(board.get_dim()):
#                if board.square(row, col) == provided.switch_player(player):
#                    print (row, col)                

#my_board = [[random.choice(range(1, 4)) for num in range(3)] for num in range(3)] 

board = [[2, 1, 3],
            [1, 2, 1],
            [1, 1, 1]]

my_board = provided.TTTBoard(3, False, board)

score_board = [[0 for dummy_row in range(3)] for dummy_col in range(3)] 

#score_board = provided.TTTBoard(3)
mc_trial(my_board, provided.PLAYERO)
mc_update_scores(score_board, my_board, provided.PLAYERO)

#print my_board