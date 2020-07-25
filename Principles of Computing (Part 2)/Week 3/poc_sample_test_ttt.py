"""
Test suite for format function in "Stopwatch - The game"
"""

import poc_simpletest
import poc_ttt_provided as provided

def run_suite(format_function):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    X = provided.PLAYERX
    O = provided.PLAYERO
    _ = provided.EMPTY
    
    #create ttt board
    A = [[O, X, X], [O, X, _], [O, O, X]] #Test #1
    B = [[O, X, X], [O, X, O], [X, O ,X]] #Test #2
    C = [[O, X, _], [O, X, X], [O, O, X]] #Test #3
    D = [[O, X, O], [O, X, X], [X, O, X]] #Test #4
    E = [[O, X, X], [O, X, O], [X, O ,X]] #Test #5
    F = [[O, X, O], [O, X, X], [X, O, X]] #Test #6
    G = [[O, X, X], [O, X, O], [_, O ,X]] #Test #7
    H = [[O, X, O], [O, X, X], [_, O ,X]] #Test #8
    I = [[O, X, _], [O, X, O], [X, O ,X]] #Test #9
    J = [[O, X, X], [O, X, _], [X, O ,X]] #Test #10
    K = [[O, X, _], [O, X, _], [_, O ,X]] #Test #11
    L = [[O, X, X], [O, X, _], [_, O ,X]] #Test #12
    M = [[O, X, _], [O, X, X], [_, O ,X]] #Test #13
    N = [[O, X, _], [O, X, _], [X, O ,X]] #Test #14
    
    # test format_function on various inputs
    suite.run_test(format_function(provided.TTTBoard(3, False, A), provided.PLAYERX), (2, (-1, -1)), "Test #1:")
    suite.run_test(format_function(provided.TTTBoard(3, False, B), provided.PLAYERO), (2, (-1, -1)), "Test #2:")
    suite.run_test(format_function(provided.TTTBoard(3, False, C), provided.PLAYERX), (2, (-1, -1)), "Test #3:")
    suite.run_test(format_function(provided.TTTBoard(3, False, D), provided.PLAYERO), (2, (-1, -1)), "Test #4:")
    suite.run_test(format_function(provided.TTTBoard(3, False, E), provided.PLAYERO), (2, (-1, -1)), "Test #5:")
    suite.run_test(format_function(provided.TTTBoard(3, False, F), provided.PLAYERO), (2, (-1, -1)), "Test #6:")
    suite.run_test(format_function(provided.TTTBoard(3, False, G), provided.PLAYERX), (2, (-1, -1)), "Test #7:")
    suite.run_test(format_function(provided.TTTBoard(3, False, H), provided.PLAYERX), (2, (-1, -1)), "Test #8:")
    suite.run_test(format_function(provided.TTTBoard(3, False, I), provided.PLAYERX), (2, (-1, -1)), "Test #9:")
    suite.run_test(format_function(provided.TTTBoard(3, False, J), provided.PLAYERX), (2, (-1, -1)), "Test #10:")
    suite.run_test(format_function(provided.TTTBoard(3, False, K), provided.PLAYERX), (2, (-1, -1)), "Test #11:")
    suite.run_test(format_function(provided.TTTBoard(3, False, L), provided.PLAYERX), (2, (-1, -1)), "Test #12:")
    suite.run_test(format_function(provided.TTTBoard(3, False, M), provided.PLAYERX), (2, (-1, -1)), "Test #13:")
    suite.run_test(format_function(provided.TTTBoard(3, False, N), provided.PLAYERX), (2, (-1, -1)), "Test #14:")


#    suite.run_test(format_function(599), "0:59.9", "Test #7:")
#    suite.run_test(format_function(600), "1:00.0", "Test #8:")
#    suite.run_test(format_function(602), "1:00.2", "Test #9:")
#    suite.run_test(format_function(667), "1:06.7", "Test #10:")
#    suite.run_test(format_function(1325), "2:12.5", "Test #11:")
#    suite.run_test(format_function(4567), "7:36.7", "Test #12:")
#    suite.run_test(format_function(5999), "9:59.9", "Test #13:")
    
    suite.report_results()	
    
    
#X = provided.PLAYERX
#O = provided.PLAYERO
#_ = provided.EMPTY
#    
#board1 = provided.TTTBoard(3, False, [[3, 2, 2], [3, 2, 1], [3, 3, 2]])
#print board1
#
#board2 = provided.TTTBoard(3, False, [[O, X, X], [O, X, _], [O, O, X]])
#print board2

#A = [[O, X, X], [O, X, _], [O, O, X]] #Test #1
#B = [[O, X, X], [O, X, O], [X, O ,X]] #Test #2
#C = [[O, X, _], [O, X, x], [O, O, X]] #Test #3
#D = [[O, X, O], [O, X, X], [X, O, X]] #Test #4
#E = [[O, X, X], [O, X, O], [X, O ,X]] #Test #5
#F = [[O, X, O], [O, X, X], [X, O, X]] #Test #6