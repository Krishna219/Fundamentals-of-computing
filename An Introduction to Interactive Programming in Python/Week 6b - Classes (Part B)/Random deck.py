import simplegui
import random

deck_of_cards = simplegui.load_image ("https://www.dropbox.com/s/wgupp562otlh07e/Deck%20of%20cards.png?dl=1")

WIDTH = deck_of_cards.get_width()
HEIGHT = deck_of_cards.get_height()

CARD_WIDTH = 167
CARD_HEIGHT = 242

HOR_CARD_SPACE = 0.5
VER_CARD_SPACE = 1
HOR_FRAME_SPACE = 5
VER_FRAME_SPACE = 5

card_center = [CARD_WIDTH / 2, CARD_HEIGHT / 2]
CARD_SIZE = [CARD_WIDTH, CARD_HEIGHT]

SCALE = 2

FRAME_SIZE = [WIDTH / SCALE, HEIGHT / SCALE]
FRAME_CENTER = [FRAME_SIZE[0] / 2, FRAME_SIZE[1] / 2]
FRAME_CARD_SIZE = [CARD_WIDTH / SCALE, CARD_HEIGHT / SCALE]

CARD_SUIT = ('C', 'D', 'H', 'S')
CARD_RANK = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')


class Card:
    def __init__(self, rank, suit):
        if rank in CARD_RANK and suit in CARD_SUIT:
            self.rank = rank
            self.suit = suit
            self.card_center = list(card_center)
            self.card_center[0] = CARD_WIDTH / 2 + CARD_RANK.index(self.rank) * ( CARD_WIDTH + HOR_CARD_SPACE)
            self.card_center[1] = CARD_HEIGHT / 2 + CARD_SUIT.index(self.suit) * ( CARD_HEIGHT + VER_CARD_SPACE)
            self.frame_center = list(FRAME_CENTER)
            
    def __str__(self):
        string1 = "---------------------------------------\nCard is '" + self.rank + "' of '" + self.suit
        string2 = "\n\nCard Rank : " + self.rank + "\nCark Suit : " + self.suit + "\nCard index : " + str(self.card_index)
        return string1 + string2
    
    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
    
    def get_index(self):
        return my_cards.index(Card)
    
    def set_index(self, index):
        self.card_index = index
    
    def draw_card(self, canvas):
        for i in range(len(my_cards)):
            if my_cards[i].suit == self.suit and my_cards[i].rank == self.rank:
                self.frame_center[0] = HOR_FRAME_SPACE + CARD_WIDTH / (2 * SCALE) + i * (HOR_FRAME_SPACE + CARD_WIDTH / SCALE)
                self.frame_center[1] = VER_FRAME_SPACE + CARD_HEIGHT / (2 * SCALE)
                canvas.draw_image(deck_of_cards,
                          self.card_center, CARD_SIZE,
                          self.frame_center, FRAME_CARD_SIZE)

def draw(canvas):
    for i in range(len(my_cards)):
        my_cards[i].draw_card(canvas)
        
frame = simplegui.create_frame("Card class", FRAME_SIZE[0], FRAME_SIZE[1])
frame.set_draw_handler(draw)
frame.start()

my_cards = [0 for i in range(2 * 4)]

for i in range(4):
    card = Card( random.choice(CARD_RANK), random.choice(CARD_SUIT))
    my_cards[i] = card
    my_cards[i + 4] = card
random.shuffle(my_cards)

