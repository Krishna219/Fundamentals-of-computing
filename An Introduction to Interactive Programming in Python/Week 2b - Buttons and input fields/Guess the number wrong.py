# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

secret_number = 0
num_range = 100
number_of_guesses = 0 

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range,secret_number,number_of_guesses
    print ""
    if(num_range == 100):
        secret_number = random.randrange(0,100)
        print "New game. Range is from 0 to 100"
    elif(num_range == 1000):
        secret_number = random.randrange(0,1000)
        print "New game. Range is from 0 to 1000"
    number_of_guesses = int(math.ceil(math.log(num_range+1)/math.log(2)))
    print "Number of remaining guesses is ",number_of_guesses

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number,number_of_guesses
    print ""
    print "Guess was ",int(guess)
    
    number_of_guesses -= 1
    print "Number of remaining guesses is ",number_of_guesses
       
    if (secret_number > int(guess)) and (number_of_guesses > 0):
        print "Higher!"
    elif (secret_number < int(guess)) and (number_of_guesses > 0):
        print "Lower!"
    elif (secret_number == int(guess)) and (number_of_guesses > 0):
        print "Correct!"
        new_game()
    elif (number_of_guesses == 0):
        print "You ran out of guesses. The number was ",secret_number
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)",range100,200)
frame.add_button("Range is [0, 1000)",range1000,200)
frame.add_input("Enter a guess",input_guess,200)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
