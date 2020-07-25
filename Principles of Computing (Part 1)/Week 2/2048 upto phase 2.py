"""
Clone of 2048 game.
"""

import random
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def shift_to_front(lst):
    """
    Function that shifts all the non-zero entries of the list 'line' to the front
    Exactly shifts all the zeros to the end
    """
    for index in range(0, len(lst) - 1):
        
        #if an element is zero just swap it with the number next to it
        
        if lst[index] == 0:
            lst[index] = lst[index + 1]
            lst[index + 1] = 0
            
            #The following code checks if the swapped element is zero 
            #And ensures all the non zero entries are at the front
            #for example [0, 0, 2, 4] the result should be [2, 4, 0, 0]
            #the above code alone will give [0, 2, 4, 0] 
            
            dummy_index = index
            
            while dummy_index > 0:
                if lst[dummy_index - 1] == 0:
                    lst[dummy_index - 1] = lst[dummy_index]
                    lst[dummy_index] = 0
                dummy_index -= 1
                
    return lst
    
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    line = list(shift_to_front(list(line)))
    
    #Code to add/ merge equal adjacent cells and place the sum in the first cell
    #replacing the second cell with zero (as per order - proceeding from left to right)
    
    for index in range(0, len(line) - 1):
        if line[index] == line[index + 1]:
            line[index] += line[index + 1]
            line[index + 1] = 0
    
    line = list(shift_to_front(list(line)))
    
    return line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Initialises the TwentyFortyEight Class
        """
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_num_2 in range(self.grid_width)] for dummy_num_1 in range(self.grid_height)]
        
        dummy_num = 0
        while dummy_num < 2:
            self.new_tile()
            dummy_num += 1

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        msg = "----------Your Gameboard----------\n"
        
        for num_1 in range(self.grid_height):
            for num_2 in range(self.grid_width):
                msg = msg + str(self.grid [num_1][num_2]) + "  "
            msg += "\n"
        return msg

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        
        #a variable to store the index of all grids containing zero
        empty_grids = []
        
        #creating a list NEW_TILE with NINE 2 and ONE 4 for getting
        #2 90% of time and 4 10% of time
        NEW_TILE = [2 for dummy_num in range(9)]
        NEW_TILE.append(4)
        
        #adds all the tiles (indexes) that contain zero to the empty_grids list
        for num_1 in range(self.grid_height):
            for num_2 in range(self.grid_width):
                if self.grid [num_1][num_2] == 0:
                    empty_grids.append((num_1, num_2))
        
        #add a randomly chosen value in NEW_TILE to 
        #randomly chosen tile in empty_grids
        chosen_grid = random.choice(empty_grids)

        self.grid[chosen_grid[0]][chosen_grid[1]] = random.choice(NEW_TILE)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid [row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid [row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

#print [merge([0, 2]),
#merge([2, 0, 2, 4]),
#merge([0, 0, 2, 2]),
#merge([2, 2, 0, 0]),
#merge([2, 2, 2, 2]),
#merge([8, 16, 16, 8, 0, 0, 8 , 16])]

#my_game = TwentyFortyEight(4, 4)
#
#print my_game
#
#my_game.set_tile(2, 3 ,16)
#
#print my_game
#
#print my_game.get_tile(2, 3)