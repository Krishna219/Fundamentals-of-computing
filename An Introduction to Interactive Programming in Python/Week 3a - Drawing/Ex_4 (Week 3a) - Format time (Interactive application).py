#import simplegui
import simplegui

#define globals
time = 0
count = 0
message = "Welcome to timer"

#define helper functions
def format_time():
    global time
    minutes = time // 60
    seconds = time % 60
    return str(minutes) + " minutes and " + str(seconds) + " seconds"

#define draw handler
def draw(canvas):
    global count
    if count == 0:
        canvas.draw_text(message, [96,190], 40, "yellow")
    else:
        canvas.draw_text(message, [10,190], 40, "yellow")

#define input handler
def get(text):
    global time, message, count
    time = int(text)
    count += 1
    message = format_time()
     
#create frame
frame = simplegui.create_frame("TIME", 480, 360)

#register event handlers
frame.set_draw_handler(draw)
frame.add_input("Enter seconds", get, 100)

#start frame
frame.start()
