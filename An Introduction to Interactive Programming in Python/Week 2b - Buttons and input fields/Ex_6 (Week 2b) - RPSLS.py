# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS

def number_to_name(name):
    if name == "Rock" or name == "rock":
        return 0
    elif name == "Spock" or name == "spock":
        return 1
    elif name == "Paper" or name == "paper":
        return 2
    elif name == "Lizard" or name == "lizard":
        return 3
    elif name == "Scissors" or name == "scissors":
        return 4
        
def name_to_number(number):
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Lizard"
    elif number == 4:
        return "Scissors"
        
def rpsls(user_guess):   
    
    user_number = number_to_name(user_guess)
    
    if(user_number != None):
        
        print "User guess is ",user_guess
    
        comp_number = random.randrange(0,5)
    
        comp_guess = name_to_number(comp_number)
    
        print "Computer guess is ",comp_guess
    
        rem = (user_number - comp_number) % 5
    
        if rem == 1 or rem == 2:
            print "User wins!"
        elif rem == 3 or rem == 4:
            print "Computer wins!"
        elif rem == 0:
            print "User and Computer tie!"
    
    else:
        
        print "Error: Bad input"
    
    print ""

# Handler for input field

def exit():
    frame.stop()

def get_guess(guess):
    rpsls(guess)
    return
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)
frame.add_button("Exit",exit,200)

# Start the frame animation
frame.start()


###################################################
# Test

#get_guess("Spock")
#get_guess("dynamite")
#get_guess("paper")
#get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
