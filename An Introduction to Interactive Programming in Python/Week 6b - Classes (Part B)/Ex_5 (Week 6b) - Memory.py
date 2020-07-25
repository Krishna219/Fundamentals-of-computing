# Add an draw method for Tile class

#################################################
# Student adds code where appropriate    

import simplegui
import random

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
EXPOSED = [True, False]
NUMBER_OF_TILES = 8
MY_LIST = range(NUMBER_OF_TILES )
MY_LIST.extend(MY_LIST)
random.shuffle(MY_LIST)
print MY_LIST

# definition of a Tile class
class Tile:
    
    # definition of intializer
    def __init__(self, num, exp, pos):
        self.number = num
        self.exposed = exp
        self.position = list(pos)

       
    # definition of getter for number
    def get_number(self):
        return self.number
    
    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed
    
    # expose the tile
    def expose_tile(self):
        self.exposed = True
    
    # hide the tile       
    def hide_tile(self):
        self.exposed = False
        
    # string method for tiles    
    def __str__(self):
        return "\nNumber   = " + str(self.number) + "\nExposed  = " + str(self.exposed) + "\nPosition = " + str(self.position) 

    # draw method for tiles
    def draw_tile(self, canvas):
        global TILE_WIDTH, TILE_HEIGHT
        
        rec_pos = [[0,0], [0,0], [0,0], [0,0]]
        rec_pos[0] = [self.position[0], self.position[1] - TILE_HEIGHT]
        rec_pos[1] = [self.position[0], self.position[1]]
        rec_pos[2] = [self.position[0] + TILE_WIDTH, self.position[1]]
        rec_pos[3] = [self.position[0] + TILE_WIDTH, self.position[1] - TILE_HEIGHT]
        
        canvas.draw_text(str(self.number), [self.position[0] + 10, self.position[1] - 30], 60, "red")
        
        if not self.is_exposed():
            canvas.draw_polygon( rec_pos, 1, "Green", "Green")
    # selection method for tiles
    def is_selected(self, pos):
        if (pos[0] > self.position[0] and pos[0] < self.position[0] + TILE_WIDTH) and (pos[1] > self.position[1] - TILE_HEIGHT and pos[1] < self.position[1]):
            return True
        else:
            return False
        

# define event handlers
def mouseclick(pos):
    for i in range(2 * NUMBER_OF_TILES):
        if my_tiles[i].is_selected(pos):
            my_tiles[i].expose_tile()
    
   
# draw handler
def draw(canvas):
    for i in range(2 * NUMBER_OF_TILES):
        my_tiles[i].draw_tile(canvas)
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * NUMBER_OF_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

# create two tiles.make sure to update initializer  
my_tiles = []

for i in range(2 * NUMBER_OF_TILES):
    tile = Tile(MY_LIST[i], False, [i * TILE_WIDTH, TILE_HEIGHT])
    print tile
    my_tiles.append(tile)

# get things rolling
frame.start()
    
    
###################################################
# Resulting frame should display a tile with number 3 (left)
# and a tile with a green back (right)
