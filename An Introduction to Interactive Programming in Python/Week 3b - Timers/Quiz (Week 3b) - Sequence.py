import simplegui

n = 13
large = 0

def update(value):
    global n
    n = value

def tick():
    global n, large
    if n > large:
        large = n
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print n, large
    if n == 1:
        timer.stop()

    
timer = simplegui.create_timer( 100, tick)

update(23)
timer.start()
