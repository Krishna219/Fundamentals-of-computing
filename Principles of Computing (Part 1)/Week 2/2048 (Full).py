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

def traverse(start_cell, direction, num_cells, test_details = False):
    """
    The function that gets all the cells from start_cell along the direction
    till num_cells is collected
    """
    cell_indexes = []
    
    for num in range(num_cells):
        row = start_cell[0] + num * direction[0]
        col = start_cell[1] + num * direction[1]
        
        #print "Processing cell ", (row, col),
        #print " Cell Value ", EXAMPLE_GRID[row][col]
        
        cell_indexes.append((row, col))

    #gives an detailed information about the particular test
    if test_details:
        msg = " Cell Indexes " + str(cell_indexes) + "\n"
        msg += " Number of Cells " +  str(num_cells) + "\n"
        return msg
    else:
        return cell_indexes
    
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Initialises the TwentyFortyEight Class
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        
        #computing the set of initial tiles for each direction 
        #That is tiles that appear first in the list that is passed 
        #to merge function
        self._initial_tiles = { UP : [(0, num) for num in range(self._grid_width)],
                        DOWN : [(self._grid_height - 1, num) for num in range(self._grid_width)],
                        LEFT : [(num, 0) for num in range(self._grid_height)],
                        RIGHT : [(num, self._grid_width - 1) for num in range(self._grid_height)]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_num_2 in range(self._grid_width)] for dummy_num_1 in range(self._grid_height)]
        
        dummy_num = 0
        while dummy_num < 2:
            self.new_tile()
            dummy_num += 1

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        msg = "----------Your Gameboard----------\n"
        
        for num_1 in range(self._grid_height):
            for num_2 in range(self._grid_width):
                msg = msg + str(self._grid [num_1][num_2]) + "  "
            msg += "\n"
        return msg

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        #the num of tiles passed to merge function may vary
        #depending on if the slide is horizontal or vertical
        #decided by the grid_height and grid_width
        
        #num_ tiles for vertical slide is grid_height
        if (direction == UP) or (direction == DOWN):
            num_tiles = self._grid_height
            
        #num_tiles for horizontal slide is grid_width
        elif (direction == LEFT) or (direction == RIGHT):
            num_tiles = self._grid_width
        
#        print self._grid
        
        for cell in self._initial_tiles[direction]:
            
            #getting the entire line in the direction with the initial tile
            #you'll get only the indexes
            line = traverse(cell, OFFSETS[direction], num_tiles)
            
            #list to store the values corresponding to the indexes
            cell_values = []
            
            #getting and storing the values in the cell_values list
            for tile in line:
                cell_values.append( self.get_tile(tile[0], tile[1]) )
           
#            print line
#            print cell_values
            
            #modify the cell_values by merging them in given direction
            cell_values = list(merge(cell_values))
#            print cell_values
#            print 
            
            for num in range(len(line)):
                self.set_tile(line[num][0], line[num][1], cell_values[num])
         
         
        self.new_tile()
#        print self._grid
            
        
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
        new_tiles = [2 for dummy_num in range(9)]
        new_tiles.append(4)
        
        #adds all the tiles (indexes) that contain zero to the empty_grids list
        for num_1 in range(self._grid_height):
            for num_2 in range(self._grid_width):
                if self._grid [num_1][num_2] == 0:
                    empty_grids.append((num_1, num_2))
        
        #add a randomly chosen value in NEW_TILE to 
        #randomly chosen tile in empty_grids
        
        if len(empty_grids) != 0:
            chosen_grid = random.choice(empty_grids)

            self._grid[chosen_grid[0]][chosen_grid[1]] = random.choice(new_tiles)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid [row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid [row][col]


#print [merge([0, 2]),
#merge([2, 0, 2, 4]),
#merge([0, 0, 2, 2]),
#merge([2, 2, 0, 0]),
#merge([2, 2, 2, 2]),
#merge([8, 16, 16, 8, 0, 0, 8 , 16])]

poc_2048_gui.run_gui(TwentyFortyEight(3, 2)) 

#print my_game
#
#my_game.set_tile(2, 3 ,16)
#
#print my_game
#
#print my_game.get_tile(2, 3)

#print traverse((0, 0), (0, 1), 4)

#print my_game
#my_game.move(UP)
#
#print my_game
#my_game.move(RIGHT)
#
#print my_game
#my_game.set_tile(0, 0, 4)
#print my_game
#my_game.move(LEFT)
#print my_game
#my_game.move(UP)
#print my_game
