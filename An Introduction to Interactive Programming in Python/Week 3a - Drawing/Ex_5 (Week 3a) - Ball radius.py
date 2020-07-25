# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    global ball_radius
    if ball_radius > 0 and ball_radius < 200:
        canvas.draw_circle([200,200], ball_radius, 5, "Green", "Blue")
    else:
        canvas.draw_text("Error: Invalid ball radius", [20,220], 30, "RED")
     
# Event handlers for buttons
def increase_radius():
    global ball_radius, RADIUS_INCREMENT
    if ball_radius <200:
        ball_radius += RADIUS_INCREMENT
    inp.set_text(str(ball_radius)) 

def decrease_radius():
    global ball_radius, RADIUS_INCREMENT
    if ball_radius > 0:
        ball_radius -= RADIUS_INCREMENT
    inp.set_text(str(ball_radius))  
    
# input handler
def inp(text):
    global ball_radius
    ball_radius = int(text)

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius, 200)
frame.add_button("Decrease radius", decrease_radius, 200)
inp = frame.add_input("Ball radius", inp, 200)
inp.set_text(str(ball_radius))

# Start the frame animation
frame.start()

