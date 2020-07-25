# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
total_ticks = 0
wins = 0
attempts = 0
milli_seconds = 0
seconds = 0
minutes = 0

#clock hand coordinates
X = 25
Y = 5
theta = 90.0
radius = 20

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def convert(value):
    if value < 10:
        return '0' + str(value)
    else:
        return str(value)

def clock_reset():
    global X, Y, theta
    X = 25
    Y = 5
    theta = 90.0
    
def update_position():
    global X, Y, theta, radius
    X = 25 + radius * math.cos(theta * math.pi / 180)
    Y = 25 - radius * math.sin(theta * math.pi / 180) 
    theta -= 0.6

def draw_clock(canvas):
    global X, Y
    canvas.draw_circle( [25,25], 20, 2, "Green")
    canvas.draw_line( [25,25], [X,Y], 4, "orange")
        
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global attempts, wins, milli_seconds
    if timer.is_running():
        timer.stop()
        attempts += 1
        if milli_seconds == 0:
            wins += 1

def reset():
    global total_ticks, wins, attempts, milli_seconds, seconds, minutes
    total_ticks = 0
    wins = 0
    attempts = 0
    milli_seconds = 0
    seconds = 0
    minutes = 0
    clock_reset()

# define event handler for timer with 0.1 sec interval
def tick():
    global total_ticks, milli_seconds, seconds, minutes
    total_ticks += 1
    milli_seconds = total_ticks % 10
    total_seconds = total_ticks // 10
    minutes = total_seconds // 60
    seconds = total_seconds % 60  
    update_position()

# define draw handler
def draw(canvas):
    global wins, attempts
    text = str(wins) + '/' + str(attempts)
    time = str(minutes) + ":" + convert(seconds) + "." + str(milli_seconds)
    canvas.draw_polygon( [(1,1), (299,1), (299,199), (1,199)], 2,"red")     
    canvas.draw_text(text, [240,30], 30, "cyan")
    canvas.draw_text(time, [70,120], 60, "yellow")
    draw_clock(canvas)
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

#create timer
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 150)
frame.add_button("Stop", stop, 150)
frame.add_button("Reset", reset, 150)


# start frame
frame.start()

# Please remember to review the grading rubric
