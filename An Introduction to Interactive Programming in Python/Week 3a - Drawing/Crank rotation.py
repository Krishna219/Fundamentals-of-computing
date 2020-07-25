import simplegui
import math

X = 230
Y = 150
theta = 0
count = 0

def tick():
    global X, Y, theta, count
    X = 180 + 80 * math.cos(theta * math.pi / 180)
    Y = 150 - 80 * math.sin(theta * math.pi / 180)
    theta += 3

def pause():
    global count
    timer.stop()
    count += 1
    
def resume():
    global count
    timer.start()
    count -= 1

def draw(canvas):
    canvas.draw_line([X,Y], [180,150], 10, "RED")
    canvas.draw_line([10,150], [260,150], 1, "orange")
    
frame = simplegui.create_frame("crank", 300, 300)
frame.set_canvas_background("White")
frame.add_button("Pause", pause, 200)
frame.add_button("Resume", resume, 200)
frame.set_draw_handler(draw)

timer = simplegui.create_timer( 100, tick)

frame.start()
timer.start()

#canvas.draw_line([10,150], [130,100], 5, "Blue") 