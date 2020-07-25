# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

color = "Red"
count = 1

# Timer handler
def tick():
    global color, count
    if count % 2 != 0:
        frame.set_canvas_background("Red")
    else:
        frame.set_canvas_background("Blue")
    count += 1
            
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.set_canvas_background("Red")
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()
