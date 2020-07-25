#import the modules
import simplegui

#loading images
deck_of_cards = simplegui.load_image ("https://www.dropbox.com/s/wgupp562otlh07e/Deck%20of%20cards.png?dl=1")

#get image constants WIDTH, HEIGHT
WIDTH = deck_of_cards.get_width()
HEIGHT = deck_of_cards.get_height()

print WIDTH, HEIGHT

#asigning image constants as CENTER and SIZE appropriately
DECK_SIZE = [WIDTH, HEIGHT]
DECK_CENTER = [WIDTH / 2, HEIGHT / 2]

#individual cards in the deck
CARD_WIDTH = 167
CARD_HEIGHT = 242
#card_center = [10 * CARD_WIDTH + CARD_WIDTH / 2  , 2 * CARD_HEIGHT + CARD_HEIGHT / 2]
card_size = [CARD_WIDTH, CARD_HEIGHT]
card_center = [12 * (167 + 0.5) + 83.5, 1 * (242 + 1) + 121]

#frame dimensions

SCALE = 2
FRAME_SIZE = [DECK_SIZE[0] / SCALE, DECK_SIZE[1] / SCALE]
frame_center = [DECK_CENTER[0] / SCALE, DECK_CENTER[1] / SCALE]

#define draw handler
def draw(canvas):
    canvas.draw_image(deck_of_cards,
                      card_center, card_size,
                      frame_center, card_size)
                      
#create frame and register handlers
frame = simplegui.create_frame("My Deck of cards", FRAME_SIZE[0], FRAME_SIZE[1], 70)
frame.set_draw_handler(draw)

#start frame
frame.start()