import simplegui

n =217

def timer_handler():
    global n
    print n
    if n % 2 == 0:
        n = n /2
    elif n % 2 != 0:
        n = 3 * n + 1
    if n == 1:
        timer.stop()
    
        

timer = simplegui.create_timer(10, timer_handler)
timer.start()