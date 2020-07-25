"""
Template for testing suite for Solitaire Mancala
"""

import random
import user39_XTtEsmjF8uqbpaz as poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # create a game
    game = game_class()
    
    # add tests using suite.run_test(....) here
    
    #1testing __init__ and __str__
    suite.run_test(str(game), str([0]))
    
    #2 testing set_board
    config = [num for num in range(10)]
    random.shuffle(config)
    
    game.set_board(config)
    
    config.reverse()
    
    suite.run_test(str(game), str(config))
    
    #3 testing get_num_seeds
    config.reverse()
    suite.run_test(game.get_num_seeds(3), config[3])
    
    #4 a, b testing is game won
    game.set_board([10,0,0,0])
    suite.run_test(game.is_game_won(), True)
    game.set_board([6, 3, 2, 3])
    suite.run_test(game.is_game_won(), False)
    
    #5 a, b testing is legal_move
    suite.run_test(game.is_legal_move(2), True)
    suite.run_test(game.is_legal_move(1), False)
    
    #6 a, b testing choose move
    suite.run_test(game.choose_move(), 2)
    game.apply_move(2)
    suite.run_test(game.choose_move(), 3)
    game.set_board([4, 3, 2, 1])
    suite.run_test(game.choose_move(), 0)
    
    #7 testing apply_move
    game.set_board([0, 1, 1, 3])
    game.apply_move(1)
    suite.run_test(str(game), str([3, 1, 0, 1]))
    game.apply_move(3)
    suite.run_test(str(game), str([0, 2, 1, 2]))
    
    #8 testing plan_moves
    game.set_board([0, 1, 1, 3])
    suite.run_test(game.plan_moves(), [1, 3, 1, 2, 1])
    game.set_board([0, 1, 2])
    suite.run_test(game.plan_moves(), [1, 2, 1])
    game.set_board([3, 0])
    suite.run_test(game.plan_moves(), [0])
    # report number of tests and failures
    suite.report_results()
    suite.test_detail()
    