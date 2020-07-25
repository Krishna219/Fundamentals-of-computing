# Polyline drawing problem

###################################################
# Student should enter code below

import simplegui
import math

polyline = []
not_close = True

# define mouseclick handler
def click(pos):
    global ployline
    polyline.append(pos)
          
# button to clear canvas
def clear():
    global polyline, not_close
    polyline = []
    not_close = True

# button to close polyline
def close():
    global polyline, not_close
    polyline.append( polyline[0])
    not_close = False

# define draw
def draw(canvas):
    global not_close
    if len(polyline) > 1:
        for point in polyline:
            canvas.draw_point( point, "red")
        
    if len(polyline) >= 2 and not_close:
        canvas.draw_polyline( polyline, 2, "green")
    
    if len(polyline) >= 2 and (not not_close):
        canvas.draw_polygon( polyline, 2, "green", "white")

# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear, 100)
frame.add_button("Close", close, 100)

# start frame
frame.start()

