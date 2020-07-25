#import modules
import simpleguitk
import random

#define global variables
height = 400
width = 500

pad_height = 80
pad_width = 15
pad1_pos = [0, 0, 0, 0]
pad2_pos = [0, 0, 0, 0]
vel = [0,0]

radius = 20
score = [0, 0]
COLOR = ['lime', 'lime']
BG_COLOR = 'white'
player = [0, 0]
tick = 0
bg = 0
c_pos = [250, 200]
c_vel = [ - random.randrange( 2, 5), - random.randrange( 1, 4)]

#paddle coordinates
pad1_pos[0] = [0, height / 2 - pad_height / 2]
pad1_pos[1] = [0, height / 2 + pad_height / 2]
pad1_pos[2] = [15, height / 2 + pad_height / 2]
pad1_pos[3] = [15, height / 2 - pad_height / 2]

pad2_pos[0] = [484, height / 2 - pad_height / 2]
pad2_pos[1] = [484, height / 2 + pad_height / 2]
pad2_pos[2] = [499, height / 2 + pad_height / 2]
pad2_pos[3] = [499, height / 2 - pad_height / 2]


#define helper functions
def new_game(direction):
    global radius, c_pos, c_vel, score
    radius = 20
    c_pos = [250, 200]
    if direction < 0:
        c_vel = [ - random.randrange( 2, 5), - random.randrange( 1, 4)]
    if direction > 0:
        c_vel = [ random.randrange( 2, 5), - random.randrange( 1, 4)]

def update_ball_pos():
    global bg, tick, c_pos, c_vel, height, width, radius, pad1_pos, score
    c_pos[0] += c_vel[0]
    c_pos[1] += c_vel[1]
    if c_pos[1] < radius or c_pos[1] > (height - radius - 1):
        c_vel[0] = c_vel[0]
        c_vel[1] = - 1.1 * c_vel[1] 
    if c_pos[0] < radius + pad_width:
        c_vel[0] = - 1.1 * c_vel[0]
        c_vel[1] = c_vel[1]
        if c_pos[1] >= pad1_pos[2][1] or c_pos[1] <= pad1_pos[3][1]:
            score[1] += 1
            new_game(c_vel[0])
            bg = 1
            tick = 0
        else:
            player[0] = 1
            player[1] = 0
            tick = 0
            bg = 0
    if c_pos[0] > (width - radius - pad_width- 1):
        c_vel[0] = - 1.1 * c_vel[0]
        c_vel[1] = c_vel[1]
        if c_pos[1] >= pad2_pos[2][1] or c_pos[1] <= pad2_pos[3][1]:
            score[0] += 1
            new_game(c_vel[0])
            bg = 1
            tick = 0
        else:
            player[0] = 0
            player[1] = 1
            tick = 0
            bg = 0

def update_pad1_pos():
    global pad1_pos, vel
    pad1_pos[0][1] += vel[0]
    pad1_pos[1][1] += vel[0]
    pad1_pos[2][1] += vel[0]
    pad1_pos[3][1] += vel[0]

def update_pad2_pos():
    global pad2_pos, vel
    pad2_pos[0][1] += vel[1]
    pad2_pos[1][1] += vel[1]
    pad2_pos[2][1] += vel[1]
    pad2_pos[3][1] += vel[1]

def timer():
    global COLOR, tick, bg, BG_COLOR
    if bg == 1 and tick < 1:
        BG_COLOR = 'black'
    elif bg == 1 and tick >= 1:
        BG_COLOR = 'white' 
    elif player[0] == 1 and tick < 2:
        COLOR[0] = 'red'      
    elif player[1] == 1 and tick < 2:
        COLOR[1] = 'red'
    else:
        COLOR = ['lime', 'lime']
    tick += 1
    
#define event handlers
def draw(canvas):
    global score, c_pos
    canvas.draw_text('Player 1', [75,30], 20, 'red')
    canvas.draw_text('Player 2', [315,30], 20, 'red')
    canvas.draw_text('Score = ' + str(score[0]), [75,60], 20, 'purple') 
    canvas.draw_text('Score = ' + str(score[1]), [315,60], 20, 'purple')
    canvas.draw_line( [15, 0], [15, 399], 2, "Fuchsia")
    canvas.draw_line( [484, 0], [484, 399], 2, "Fuchsia")
    canvas.draw_line( [250, 0], [250, 399], 2, "blue")
    canvas.draw_circle( c_pos, radius, 2, "red", "cyan")
    canvas.draw_polygon( [ pad1_pos[0], pad1_pos[1], pad1_pos[2], pad1_pos[3] ], 2, "blue", COLOR[0])
    canvas.draw_polygon( [ pad2_pos[0], pad2_pos[1], pad2_pos[2], pad2_pos[3] ], 2, "blue", COLOR[1])
    frame.set_canvas_background(BG_COLOR)
    update_ball_pos()
    if pad1_pos[0][1] > 2 and pad1_pos[1][1] < 397:
        update_pad1_pos()
    if pad2_pos[0][1] > 2 and pad2_pos[1][1] < 397:
        update_pad2_pos()
    
def key_down(key):
    global vel
    if key == simpleguitk.KEY_MAP [ "w" ] and pad1_pos[0][1] > 2:
        vel[0] += -5
        update_pad1_pos()
    if key == simpleguitk.KEY_MAP [ "s" ] and pad1_pos[1][1] < 397:
        vel[0] += 5
        update_pad1_pos()
    if key == simpleguitk.KEY_MAP [ "up" ] and pad2_pos[0][1] > 2:
        vel[1] += -5
        update_pad2_pos()
    if key == simpleguitk.KEY_MAP [ "down" ] and pad2_pos[1][1] < 397:
        vel[1] += 5
        update_pad2_pos()    
    
def key_up(key):
    global vel
    if key == simpleguitk.KEY_MAP [ "w" ] or key == simpleguitk.KEY_MAP [ "s" ]:
        vel[0] = 0
    if key == simpleguitk.KEY_MAP [ "up" ] or key == simpleguitk.KEY_MAP [ "down" ]:
        vel[1] = 0

def reset():
    global score
    score = [0, 0]
    new_game(random.randrange(-1, 2, 2))

    
#create frame
frame = simpleguitk.create_frame( "Motion", 500, 400) 
timer = simpleguitk.create_timer(100, timer)

#register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.add_button("New Game", reset, 150)

#start frame
frame.start()
timer.start()

new_game(random.randrange(-1, 2, 2))
