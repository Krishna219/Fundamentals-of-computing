# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def timer():
    global radius, HEIGHT
    if radius < (HEIGHT / 2):
        radius += 1
    
# Draw handler
def draw(canvas):
    canvas.draw_circle([100,100], radius, 3, "RED")
        
# Create frame and timer
frame = simplegui.create_frame("Expanding circle", WIDTH, HEIGHT)
timer = simplegui.create_timer(100, timer)
frame.set_draw_handler(draw)

# Start timer
frame.start()
timer.start()