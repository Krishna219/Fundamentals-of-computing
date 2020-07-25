#import modules
import simplegui

#define global variables
pos = [250, 200]
vel = [0, 0]

#define helper functions
def update_pos():
    global pos, vel
    pos[0] += vel[0]
    pos[1] += vel[1]
    if pos[1] < 20 or pos[1] > (400 - 20):
        vel[0] = vel[0]
        vel[1] = - 1.2 * vel[1] 
    if pos[0] < 20 or pos[0] > (500 - 20):
        vel[0] = - 1.2 * vel[0]
        vel[1] = vel[1]

#define event handlers
def draw(canvas):
    canvas.draw_circle( pos, 20, 2, "red", "cyan")
    update_pos()
    
def key_down(key):
    global pos
    if key == simplegui.KEY_MAP [ "up" ]:
        vel[1] -= 1
    if key == simplegui.KEY_MAP [ "left" ]:
        vel[0] -= 1
    if key == simplegui.KEY_MAP [ "down" ]:
        vel[1] += 1
    if key == simplegui.KEY_MAP [ "right" ]:
        vel[0] += 1

def key_up(key):   
    global pos
    if key == simplegui.KEY_MAP [ "up" ]:
        vel[1] = 0
    if key == simplegui.KEY_MAP [ "left" ]:
        vel[0] = 0
    if key == simplegui.KEY_MAP [ "down" ]:
        vel[1] = 0
    if key == simplegui.KEY_MAP [ "right" ]:
        vel[0] = 0

#create frame
frame = simplegui.create_frame( "Motion", 500, 400) 

#register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)

#start frame
frame.start()