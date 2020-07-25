# Ball grid slution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw

def draw(canvas):
    global BALL_RADIUS
    ball_pos = [0, 0]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            ball_pos[0] = 2 * i * BALL_RADIUS + BALL_RADIUS
            ball_pos[1] = 2 * j * BALL_RADIUS + BALL_RADIUS
            canvas.draw_circle( ball_pos, BALL_RADIUS, 2, "Black", "Red")

# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_canvas_background("white")

# start frame
frame.start()

