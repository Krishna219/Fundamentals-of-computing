# -*- coding: utf-8 -*-
"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

##import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # replace with your code
        invariant = True
        
#        print (target_row, target_col)
        #check if Tile zero is positioned at (i,j)
        if self._grid[target_row][target_col] != 0:
            return False
        
        #All tiles in rows i+1 or below are positioned at their solved location
        for row in range(target_row + 1, self._height):
            for col in range(self._width):
#                print (row, col),
                if self.current_position(row, col) != (row, col):
                    return False
        
        #All tiles in row i to the right of position (i,j) are positioned at their solved location.        
        for col in range(target_col + 1, self._width):
#            print (target_row, col),
            if self.current_position(target_row, col) != (target_row, col):
                return False
                
        return invariant
    
    def position_tile(self, tile_pos, req_pos):
        """
        Positions the given tile at the required position
        tile_pos - tile to be positioned
        req_pos - required position
        returns a move string
        """
        tot_moves = ""
        target_row = tile_pos[0]
        target_col = tile_pos[1]
        
        current_position = self.current_position(target_row, target_col)
        
        return ""
    
    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        
        assert target_row > 1 and target_col > 0
        
        #check invariant
        assertion_error  = "Exception lower row invariant is False at " + str((target_row, target_col))
        assert self.lower_row_invariant(target_row, target_col), assertion_error

        tot_moves = ""
        
        current_position = self.current_position(target_row, target_col)
        
        assert (current_position[0] < target_row) or ((current_position[0] == target_row) and (current_position[1] < target_col))
        
        #find relative position of target tile with respect to zero tile
        relative_pos = (current_position[0] - target_row, current_position[1] - target_col)
        
        
        #Three cases of solving based on relative position
        if relative_pos[0] == 0: #tile lies in same row as target row
            
            move = ""
            
            #move zero tile left to the target cell position
            for dummy_i in range(relative_pos[1], 0):
                move += "l"
                
#            tot_moves += move
            
            #move the target tile right use "urrdl"
#            move = ""
            for dummy_i in range(relative_pos[1], -1):
                move += "urrdl"
                
            tot_moves += move    
            
        elif relative_pos[1] == 0:#tile lies in same col as target col
            
            move = ""
            
            #move zero tile up to the target cell position
            for dummy_i in range(relative_pos[0], 0):
                move += "u"
                
#            tot_moves += move
            
            #move the target tile down use "lddru"
#            move = ""
            for dummy_i in range(relative_pos[0], -1):
                move += "lddru"
                
#            tot_moves += move    
            
            #move zero tile to the left of target tile
            move += "ld"
            
            tot_moves += move    
            
        else:
            
            move = ""
            
            #move zero tile to the target cell position
            if relative_pos[1] < 0:
                for dummy_i in range(relative_pos[0], 0):
                    move += "u"
                for dummy_i in range(relative_pos[1], 0):
                    move += "l"
                
                #move target tile right
                for dummy_i in range(relative_pos[1], -1):
                    if current_position[0] == 0:
                        move += "drrul"
                    else:
                        move += "urrdl"
                    
            else:
                for dummy_i in range(relative_pos[0], 0):
                    move += "u"
                for dummy_i in range(relative_pos[1]):
                    move += "r"
                    
                #move target tile left                               
                for dummy_i in range(1, relative_pos[1]):
                    if current_position[0] == 0:
                        move += "dllur"
                    else:
                        move += "ulldr"
                        
                #place zero tile left of target
                if current_position[0] == 0:
                    move += "dllu"
                else:
                    move += "ulld"

            #move target tile down
            move += "dru"
            
            for dummy_i in range(relative_pos[0], -1):
                move += "lddru"
                
            #move zero tile to the left of target tile
            move += "ld"
            
            tot_moves += move
                
        self.update_puzzle(tot_moves)
#        print str(self)
#        print tot_moves
        #check invariant
        assertion_error  = "Exception lower row invariant is False at " + str((target_row, target_col - 1))
        assert self.lower_row_invariant(target_row, target_col - 1), assertion_error
        
        #move zero cell to target tile
        return tot_moves

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        
        assert target_row > 1
        
        target_col = 0
        
        #check invariant
        assertion_error  = "Exception lower row invariant is False at " + str((target_row, target_col))
        assert self.lower_row_invariant(target_row, target_col), assertion_error
        
        tot_moves = ""
        
        current_position = self.current_position(target_row, target_col)
        
        #move the zero tile from (i,0) to (i−1,1) using the move string "ur"
        tot_moves += "ur"
        
        self.update_puzzle(tot_moves)
        print str(self)
        print tot_moves
        
        current_zero_position = self.current_position(0, 0)
        
        print current_position, current_zero_position
        
        #find relative position of target tile with respect to zero tile
        relative_pos = (current_position[0] - target_row, current_position[1] - target_col)
        
        #check invariant
#        assertion_error  = "Exception lower row invariant is False at " + str((target_row - 1, self._width - 1))
#        assert self.lower_row_invariant(target_row - 1, self._width - 1), assertion_error

        return tot_moves

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

#lower row invariant tests
#my_puzzle = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
##my_puzzle = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#print my_puzzle
#print my_puzzle.lower_row_invariant(2, 2)

#solve interior tile tests
#my_puzzle1 = Puzzle(3, 3, [[7, 1, 6], [5, 4, 3], [2, 0, 8]])
#my_puzzle2 = Puzzle(3, 3, [[6, 1, 2], [5, 4, 3], [8, 7, 0]])
#my_puzzle3 = Puzzle(3, 3, [[1, 7, 6], [5, 4, 3], [2, 0, 8]]) 
#my_puzzle4 = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
#my_puzzle5 = Puzzle(3, 3, [[7, 1, 6], [5, 4, 3], [2, 0, 8]])
#
#print my_puzzle2
#str2 = my_puzzle2.solve_interior_tile(2, 2) #llurrdl
#print str2 
#print "Test #2 :", "Success" if str2 == "llurrdl" else "Failure"
#print
#print my_puzzle3
#str3 = my_puzzle3.solve_interior_tile(2, 1) #uulddruld
#print str3 
#print "Test #3 :", "Success" if str3 == "uulddruld" else "Failure"
#print
#print my_puzzle4
#str4 = my_puzzle4.solve_interior_tile(2, 2) #uulldrruldrulddruld
#print str4 
#print "Test #4 :", "Success" if str4 == "uulldrruldrulddruld" else "Failure"
#print
#print my_puzzle1
#str1 = my_puzzle1.solve_interior_tile(2, 1) #uuldrulddruld
#print str1
#print "Test #1 :", "Success" if str1 == "uuldrulddruld" else "Failure"
#print

#solve col0 tile
my_puzzle1 = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [0, 7, 8]])
print my_puzzle1.solve_col0_tile(2)

