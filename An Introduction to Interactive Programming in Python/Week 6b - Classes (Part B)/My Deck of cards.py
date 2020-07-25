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

#frame dimensions

SCALE = 2
FRAME_SIZE = [DECK_SIZE[0] / SCALE, DECK_SIZE[1] / SCALE]
frame_center = [DECK_CENTER[0] / SCALE, DECK_CENTER[1] / SCALE]

#define draw handler
def draw(canvas):
    canvas.draw_image(deck_of_cards,
                      DECK_CENTER, DECK_SIZE,
                      frame_center, FRAME_SIZE)
                      
#create frame and register handlers
frame = simplegui.create_frame("My Deck of cards", FRAME_SIZE[0], FRAME_SIZE[1], 70)
frame.set_draw_handler(draw)

#start frame
frame.start()