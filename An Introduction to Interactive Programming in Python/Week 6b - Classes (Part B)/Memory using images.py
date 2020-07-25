#import modules
import simplegui
import random
import math

#load image
tile_cover = simplegui.load_image("https://www.dropbox.com/s/ukemajgulc175en/BicycleStandardBlue_4.jpg?dl=1")
deck_of_cards = simplegui.load_image ("https://www.dropbox.com/s/wgupp562otlh07e/Deck%20of%20cards.png?dl=1")

#define globals
turns = 0

CARD_SUIT = ('C', 'D', 'H', 'S')
CARD_RANK = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

NUMBER_OF_TILES = 2
EXPOSED = [True, False]
MY_LIST = ['2', '3', '4', '5', '6', '7', '8', '9']
MY_LIST.extend( ['2', '3', '4', '5', '6', '7', '8', '9'])
random.shuffle(MY_LIST)

TILE_WIDTH = 60
TILE_HEIGHT = 100

WIDTH = tile_cover.get_width()
HEIGHT = tile_cover.get_height()

TILE_COVER_CENTER = [WIDTH / 2, HEIGHT /2]
TILE_COVER_SIZE = [WIDTH, HEIGHT]

CARD_WIDTH = 167
CARD_HEIGHT = 242

HOR_CARD_SPACE = 0.5
VER_CARD_SPACE = 1
HOR_FRAME_SPACE = 10
VER_FRAME_SPACE = 10

EXPOSED_CIRCLE_CENTER = [420, 220]
RESET_CIRCLE_CENTER = [EXPOSED_CIRCLE_CENTER[0], EXPOSED_CIRCLE_CENTER[1] + 60]
CIRCLE_RADIUS = 10

#define classes
class Card:
    def __init__(self, num):
            self.rank = str(num)
            self.suit = random.choice(CARD_SUIT)
    
    def __str__(self):
        string = "------------------------------\nCard rank : " + self.rank 
        return string
    
    def draw(self, canvas, pos):
        card_center = [CARD_WIDTH / 2 + CARD_RANK.index(self.rank) * (CARD_WIDTH + HOR_CARD_SPACE),
                       CARD_HEIGHT / 2 + CARD_SUIT.index(self.suit) * (CARD_HEIGHT + VER_CARD_SPACE)]
        frame_center = [TILE_WIDTH / 2 + (pos[0] / TILE_WIDTH - 1) * (TILE_WIDTH + HOR_FRAME_SPACE),
                        TILE_HEIGHT / 2 + (pos[1] / TILE_HEIGHT - 1) * (TILE_HEIGHT + VER_FRAME_SPACE)]
        canvas.draw_image(deck_of_cards,
                          card_center, [CARD_WIDTH, CARD_HEIGHT],
                          frame_center, [TILE_WIDTH, TILE_HEIGHT])
        
    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit
                          

class Tile:
    def __init__(self, num, exp, pos):
        self.number = num       
        self.card = Card(self.number)
        self.position = list(pos)
        self.exposed = exp
    
    def __str__(self):
        string = "------------------------------\nCard number : " + str(self.number) + "\nExposed     : " + str(self.exposed) + "\nPosition    : " + str(self.position)
        return string
    
    def get_number(self):
        return self.number
    
    def is_exposed(self):
        return self.exposed
    
    def expose_tile(self):
        self.exposed = True
        
    def hide_tile(self):
        self.exposed = False
    
    def draw(self, canvas):
        
        self.card.draw(canvas, self.position)
        if not self.is_exposed():
            frame_center = [TILE_WIDTH / 2 + (self.position[0] / TILE_WIDTH  -1) * (TILE_WIDTH + HOR_FRAME_SPACE),
                        TILE_HEIGHT / 2 + (self.position[1] / TILE_HEIGHT -1) * (TILE_HEIGHT + VER_FRAME_SPACE)]
            canvas.draw_image(tile_cover,
                              TILE_COVER_CENTER, TILE_COVER_SIZE,
                              frame_center, [TILE_WIDTH, TILE_HEIGHT])
            
    def is_selected(self, pos):
        i = self.position[0] / TILE_WIDTH - 2
        j = self.position[1] / TILE_HEIGHT - 2
        hor_limits = [self.position[0] + i * HOR_FRAME_SPACE - TILE_WIDTH, self.position[0] + i * HOR_FRAME_SPACE]
        ver_limits = [self.position[1] + j * VER_FRAME_SPACE - TILE_HEIGHT, self.position[1] + j * VER_FRAME_SPACE]
        if (pos[0] > hor_limits[0] and pos[0] < hor_limits[1]) and (pos[1] > ver_limits[0] and pos[1] < ver_limits[1]):
            return True
        else:
            return False

#define helper functions   
def distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 +(x[1] - y[1]) ** 2)        

def new_game():
    global label, previous_cards, card_positions, clicks, turns, tenth_second, my_tiles, EXPOSED_CIRCLE_FILL_COLOR, RESET_CIRCLE_FILL_COLOR, MY_LIST
    previous_cards = [0, 0]
    card_positions = [0, 0]
    clicks = 0
    turns = 0
    label.set_text("Turns " + str(turns))
    tenth_second = 0
    my_tiles = []
    EXPOSED_CIRCLE_FILL_COLOR = "black"
    RESET_CIRCLE_FILL_COLOR = "black"
    random.shuffle(MY_LIST)
    for j in range(len(MY_LIST) / 4):
        for i in range(len(MY_LIST) / 4):
            my_tile = Tile(MY_LIST[j * 4 + i], False, [(i + 2) * TILE_WIDTH, (j + 2) * TILE_HEIGHT])
            my_tiles.append(my_tile)
            
#define event handlers
def draw(canvas):
    canvas.draw_text("Memory Game", [100, 60], 60, "purple")
    if tenth_second <= 2:
        canvas.draw_circle(RESET_CIRCLE_CENTER, CIRCLE_RADIUS, 2, "red", "cyan")
    else:
        canvas.draw_circle(RESET_CIRCLE_CENTER, CIRCLE_RADIUS, 2, "red", RESET_CIRCLE_FILL_COLOR)
    canvas.draw_text("Turns " + str(turns), [EXPOSED_CIRCLE_CENTER[0] + 30, EXPOSED_CIRCLE_CENTER[1] + 120], 25, "blue")
    canvas.draw_text("New Game", [RESET_CIRCLE_CENTER[0] + 30, RESET_CIRCLE_CENTER[1] + 5], 25, "Blue")
    canvas.draw_circle(EXPOSED_CIRCLE_CENTER, CIRCLE_RADIUS, 2, "red", EXPOSED_CIRCLE_FILL_COLOR)
    canvas.draw_text("Expose All", [EXPOSED_CIRCLE_CENTER[0] + 30, EXPOSED_CIRCLE_CENTER[1] + 5], 25, "Blue")
    for i in range(len(MY_LIST)):
        my_tiles[i].draw(canvas)

def expose_all():
    global EXPOSED_CIRCLE_FILL_COLOR
    for i in range(len(MY_LIST)):
        my_tiles[i].expose_tile()
    EXPOSED_CIRCLE_FILL_COLOR = "cyan"

def click(pos):
    global label, EXPOSED_CIRCLE_FILL_COLOR, turns, previous_cards, card_positions, clicks, turns
    if (distance(pos, EXPOSED_CIRCLE_CENTER) <= CIRCLE_RADIUS):
        for tile in my_tiles:
            tile.expose_tile()
        EXPOSED_CIRCLE_FILL_COLOR = "cyan"
    if distance(pos, RESET_CIRCLE_CENTER) <= CIRCLE_RADIUS:
        new_game()
    for tile in my_tiles:
        if tile.is_selected(pos):
            if not tile.is_exposed():
                tile.expose_tile()
                if clicks < 2:
                    if clicks == 1:
                        turns += 1
                        label.set_text("Turns " + str(turns))
                    previous_cards[clicks] = tile.number
                    card_positions[clicks] = tile.position
                    clicks += 1
                else:
                    if previous_cards[0] != previous_cards[1]:
                        for i in range(len(my_tiles)):
                            if my_tiles[i].position == card_positions[0] or my_tiles[i].position == card_positions[1]:
                                my_tiles[i].hide_tile()
                    clicks = 0
                    previous_cards = [0, 0]
                    card_positions = [0, 0]
                    previous_cards[clicks] = tile.number
                    card_positions[clicks] = tile.position 
                    clicks += 1  
        
def reset():
    new_game()
    
def tick():
    global tenth_second
    tenth_second += 1
    pass
        
#create frame and register event handlers


frame = simplegui.create_frame("Memory" , 600, 600)
frame.set_draw_handler(draw)
frame.set_canvas_background("Green")
frame.add_button("Expose All", expose_all, 150)
frame.set_mouseclick_handler(click)
frame.add_button("New Game", reset, 150)
label = frame.add_label("Turns " + str(turns))

#create timer
timer = simplegui.create_timer(100, tick)
timer.start()

#start frame
frame.start()

new_game()
