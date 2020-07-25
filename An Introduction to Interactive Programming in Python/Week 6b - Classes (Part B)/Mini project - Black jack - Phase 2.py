# Mini-project #6 - Blackjack

import simplegui
import random
import math

# load card sprite
center_image = simplegui.load_image("https://www.dropbox.com/s/sv4dl2mz4dmllaz/at-casino-com-logo.png?dl=1")

center_image_width = center_image.get_width()
center_image_height = center_image.get_height()
#print[center_image_width, center_image_height]
 
center_image_size = [center_image_width, center_image_height]

center_image_position = [center_image_width / 2, center_image_height / 2]

black_jack = simplegui.load_image("https://www.dropbox.com/s/2qtetx7kgtto1xg/Logo.png?dl=1")

black_jack_width = black_jack.get_width()
black_jack_height = black_jack.get_height()
#print black_jack_width, black_jack_height

black_jack_size =  [black_jack_width, black_jack_height]
black_jack_center = [ black_jack_width / 2, black_jack_height / 2]

support_message = "New Deal?"

CARD_SIZE = (167, 242)
CARD_CENTER = (83.5, 121)
card_images = simplegui.load_image("https://www.dropbox.com/s/wgupp562otlh07e/Deck%20of%20cards.png?dl=1")

CARD_BACK_SIZE = (866, 1200)
CARD_BACK_CENTER = (433, 600)
card_back = simplegui.load_image("https://www.dropbox.com/s/ukemajgulc175en/BicycleStandardBlue_4.jpg?dl=1")    

TILE_WIDTH = 115
TILE_HEIGHT = 160

HOR_CARD_SPACE = 0.5
VER_CARD_SPACE = 1.5
HOR_FRAME_SPACE = 20

DEALER_CARD_POSITION = [TILE_WIDTH , 1.5 * TILE_HEIGHT]
PLAYER_CARD_POSITION = [TILE_WIDTH , 3 * TILE_HEIGHT]

ticks = 0
you_lose = False

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
NEW_GAME_CIRCLE_CENTER = [800, 450]
DEAL_CIRCLE_CENTER = [800, 500]
HIT_CIRCLE_CENTER = [800, 550]
STAND_CIRCLE_CENTER = [800, 600]

NEW_GAME_COLOR = "black"
DEAL_COLOR = "black"
HIT_COLOR = "black"
STAND_COLOR = "black"

RADIUS = 10

# define globals for cards
SUITS = ('C', 'D', 'H', 'S')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + (CARD_SIZE[0] + HOR_CARD_SPACE) * RANKS.index(self.rank), 
                    CARD_CENTER[1] + (CARD_SIZE[1] + VER_CARD_SPACE)* SUITS.index(self.suit))
        if CARD_SIZE[0] > 0 and CARD_SIZE[1] > 0:
            canvas.draw_image(card_images, 
                          card_loc, CARD_SIZE, 
                          pos, [TILE_WIDTH, TILE_HEIGHT])
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []
        self.value = 0

    def __str__(self):
        # return a string representation of a hand
        string = "Hand contains "
        for card in self.hand:
            string += card.get_suit() + card.get_rank() + " "
        return string

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        for card in self.hand:
            hand_value += VALUES[card.get_rank()]
        for card in self.hand:
            if card.get_rank() == 'A':
                if hand_value + 10 <= 21:
                    return hand_value + 10
                else:
                    return hand_value                 
        return hand_value
    
    def draw(self, canvas, pos):
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, 
                                 [(pos[0] + HOR_FRAME_SPACE)* i + pos[0], 
                                  pos[1]]) 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        string = "Deck contains "
        for card in self.deck:
            string += card.get_suit() + card.get_rank() + " "
        return string        


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score, support_message, you_lose, ticks
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    if in_play:
        support_message = "You lose!!!"
        you_lose = True
        ticks = 0
        score -= 1
    for i in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    # your code goes here
    
    in_play = True

def hit():
    global deck, player_hand, dealer_hand, in_play, message, support_message, score
    # replace with your code below
    if player_hand.get_value() <= 21:
        if in_play:
            player_hand.add_card(deck.deal_card())
    if player_hand.get_value() > 21:
        if in_play:
            score -= 1
            in_play = False
            message = "You are Busted"
            support_message = "New Deal ?"
    
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global deck, player_hand, dealer_hand, message, in_play, score, support_message
    # replace with your code below
    if player_hand.get_value() > 21:
        message = "Dude!You are Busted!!!"
    else:
        while dealer_hand.get_value() <= 17:
            if in_play:
                dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21: 
            if in_play:
                score += 1
            message = "Dealer is Busted. You win!!!"
        else:
            if dealer_hand.get_value() < player_hand.get_value():
                if in_play:
                    score += 1
                message = "You are the Winner!!!"
            elif dealer_hand.get_value() > player_hand.get_value():
                if in_play:
                    score -= 1
                message = "Dealer Wins!!!"
            else:
                message = "Wow! It's a Tie!!!"
    in_play = False 
    support_message = "New Deal ?"
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
def distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 +(x[1] - y[1]) ** 2)

def new_game():
    global score, message, in_play
    score = 0
    message = "New Deal?"
    in_play = False
    deal()

def click(pos):
    global ticks, DEAL_COLOR, NEW_GAME_COLOR, HIT_COLOR, STAND_COLOR, RADIUS
    if distance(pos, NEW_GAME_CIRCLE_CENTER) <= RADIUS:
        new_game()
        NEW_GAME_COLOR = "lime"
        ticks = 0
    if distance(pos, DEAL_CIRCLE_CENTER) <= RADIUS:
        deal()
        DEAL_COLOR = "lime"
        ticks = 0
    if distance(pos, HIT_CIRCLE_CENTER) <= RADIUS:
        hit()
        HIT_COLOR = "lime"
        ticks = 0
    if distance(pos, STAND_CIRCLE_CENTER) <= RADIUS:
        stand()
        STAND_COLOR = "lime"
        ticks = 0

def tick():
    global ticks, DEAL_COLOR, NEW_GAME_COLOR, HIT_COLOR, STAND_COLOR, you_lose
    if ticks > 2 and NEW_GAME_COLOR == "lime":
        NEW_GAME_COLOR = "black"
    if ticks > 2 and DEAL_COLOR == "lime":
        DEAL_COLOR = "black"
    if ticks > 2 and HIT_COLOR == "lime":
        HIT_COLOR = "black"
    if ticks > 2 and STAND_COLOR =="lime":
        STAND_COLOR = "black"
    if ticks > 10 and you_lose:
        you_lose = False
    ticks += 1
    
        
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    # draw a hand on the canvas, use the draw method for cards
    global you_lose, score, player_hand, dealer_hand, in_play, message, support_message, NEW_GAME_CIRCLE_CENTER, DEAL_CIRCLE_CENTER, HIT_CIRCLE_CENTER, STAND_CIRCLE_CENTER, RADIUS
    canvas.draw_text("Score : " + str(score), [750, 60], 50, "pink")
    canvas.draw_text("New Game",[800 + 30, 450 + 10], 30, "orange")
    canvas.draw_text("Deal",[800 + 30, 500 + 10], 30, "orange")
    canvas.draw_text("Hit",[800 + 30, 550 + 10], 30, "orange")
    canvas.draw_text("Stand",[800 + 30, 600 + 10], 30, "orange")
    canvas.draw_circle(NEW_GAME_CIRCLE_CENTER, RADIUS, 2, "red", NEW_GAME_COLOR)
    canvas.draw_circle(DEAL_CIRCLE_CENTER, RADIUS, 2, "red", DEAL_COLOR)
    canvas.draw_circle(HIT_CIRCLE_CENTER, RADIUS, 2, "red", HIT_COLOR)
    canvas.draw_circle(STAND_CIRCLE_CENTER, RADIUS, 2, "red", STAND_COLOR)
    
    if black_jack_size[0] > 0 and black_jack_size[1] >0:
        canvas.draw_image(black_jack,
                          black_jack_center, black_jack_size,
                          [512, 50], [339, 130])
    if center_image_size[0] > 0 and center_image_size[1] > 0:
        canvas.draw_image(center_image,
                          center_image_position, center_image_size,
                          [512, 360], [center_image_size[0] * 1.3, center_image_size[1] * 1.3])
    dealer_hand.draw(canvas, DEALER_CARD_POSITION)
    player_hand.draw(canvas, PLAYER_CARD_POSITION) 
    if in_play: 
        canvas.draw_image(card_back,
                          CARD_BACK_CENTER, CARD_BACK_SIZE,
                          DEALER_CARD_POSITION, [TILE_WIDTH, TILE_HEIGHT])
        canvas.draw_text("Hit or stand ?", [3 * TILE_WIDTH + 4 * HOR_FRAME_SPACE, 0.9 * TILE_HEIGHT], 50, "cyan")
        if you_lose:
            canvas.draw_text(support_message, [6 * TILE_WIDTH + 4 * HOR_FRAME_SPACE, 1.3 * TILE_HEIGHT], 50, "lime")
    else:
        canvas.draw_text(support_message, [6 * TILE_WIDTH + 4 * HOR_FRAME_SPACE, 1.3 * TILE_HEIGHT], 50, "lime")
        canvas.draw_text(message, [3 * TILE_WIDTH + 4 * HOR_FRAME_SPACE, 0.9 * TILE_HEIGHT], 50, "cyan")
    canvas.draw_text("Dealers hand", [TILE_WIDTH * 0.3, TILE_HEIGHT * 0.9], 50, "Blue")
    canvas.draw_text("Players hand", [TILE_WIDTH * 0.3, TILE_HEIGHT * 2.4], 50, "Blue")

# initialization frame
frame = simplegui.create_frame("Blackjack", 1024, 720)
frame.set_canvas_background("green")

#timer
timer = simplegui.create_timer(100, tick)

#create buttons and canvas callback
frame.add_button("New game", new_game, 150)
frame.add_button("Deal", deal, 150)
frame.add_button("Hit",  hit, 150)
frame.add_button("Stand", stand, 150)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)


# get things rolling
new_game()
frame.start()
timer.start()

# remember to review the gradic rubric