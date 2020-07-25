# Echo mouse click in console

###################################################
# Student should enter code below

import simplegui

pos = []

def click(position):
    global pos
    pos = position
    
def draw(canvas):
    canvas.draw_text("Mouse click at " + str( pos ), [200, 200], 30, "Red")

frame = simplegui.create_frame( "Mouse Click", 640, 420)
frame.set_canvas_background("white")
frame.start()

frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

###################################################
# Sample output

#Mouse click at (104, 105)
#Mouse click at (169, 175)
#Mouse click at (197, 135)
#Mouse click at (176, 111)
#Mouse click at (121, 101)
#Mouse click at (166, 208)
#Mouse click at (257, 235)
#Mouse click at (255, 235)