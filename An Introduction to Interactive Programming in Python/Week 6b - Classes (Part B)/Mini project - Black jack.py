# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (167, 242)
CARD_CENTER = (83.5, 121)
card_images = simplegui.load_image("https://www.dropbox.com/s/wgupp562otlh07e/Deck%20of%20cards.png?dl=1")

CARD_BACK_SIZE = (866, 1200)
CARD_BACK_CENTER = (433, 600)
card_back = simplegui.load_image("https://www.dropbox.com/s/ukemajgulc175en/BicycleStandardBlue_4.jpg?dl=1")    

HOR_CARD_SPACE = 0.5
VER_CARD_SPACE = 1.5
# initialize some useful global variables
in_play = False
outcome = ""
score = 0

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
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
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
            else:
                return hand_value                 
        return hand_value
    
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
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
    global outcome, in_play, deck, player_hand, dealer_hand
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    
    for i in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    
    print player_hand
    print dealer_hand 
    print "-----------------------------------"

    # your code goes here
    
    in_play = True

def hit():
    global deck, player_hand, dealer_hand
    # replace with your code below
    if player_hand.get_value() <= 21:
        player_hand.add_card(deck.deal_card())
    if player_hand.get_value() > 21:
        print "You are Busted"
        print "-----------------------------------"
    else:
        print player_hand
        print dealer_hand 
        print "-----------------------------------"
    
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global deck, player_hand, dealer_hand
    # replace with your code below
    if player_hand.get_value() > 21:
        print "You are Busted"
        print "-----------------------------------"
    else:
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())
        print player_hand
        print dealer_hand 
        print "-----------------------------------"
        if dealer_hand.get_value() > 21:
            print "Dealer is Busted. You win!!!"
            print "-----------------------------------"
        else:
            if dealer_hand.get_value() < player_hand.get_value():
                print "You are the Winner!!!"
                print "-----------------------------------"
            elif dealer_hand.get_value() > player_hand.get_value():
                print "Dealer Wins!!!"
                print "-----------------------------------"
            else:
                print "Wow! It's a Tie!!!"
                print "-----------------------------------"
            
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "K")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric