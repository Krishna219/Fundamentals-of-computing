# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui 

total_ticks = 0
first_click = True


#convert seconds
def conv(val):
    if val < 10:
        return "0" + str(val)
    else:
        return str(val)

# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
    tenth_seconds = total_ticks % 10
    seconds = total_ticks // 10
    minutes = seconds // 60
    seconds = seconds % 60
    print conv(minutes) + ":" + conv(seconds) + "." + str(tenth_seconds)
    
# Button handler
def click():
    global first_click, total_ticks
    if first_click:
        timer.start()
        first_click = False
    else:
        timer.stop()
        first_click = True
        tenth_seconds = total_ticks % 10
        seconds = total_ticks // 10
        minutes = seconds // 60
        seconds = seconds % 60
        print conv(minutes) + ":" + conv(seconds) + "." + str(tenth_seconds)
        total_ticks = 0

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(100, tick)

# Start timer
frame.start()
