import simplegui
import random

list_1 = range(0, 8)
list_1.extend(range(0, 8))
exposed = [ False for i in range(0, 16)]
rec = [ [0, 0], [0, 100], [50, 100], [50, 0]]
rec_color = [ "yellow" for i in range(0, 16) ]
rec_color_code = [ 2 for i in range(0, 16) ]
turn = 0
tick = 0
turn = 0
count = 0
card = [0, 0]
card_index = [0, 0]
random.shuffle(list_1)

def new_game():
    global list_1, exposed, rec, rec_color, rec_color_code, turn, tick, card, card_index, count
    list_1 = range(0, 8)
    list_1.extend(range(0, 8))
    exposed = [ False for i in range(0, 16)]
    rec = [ [0, 0], [0, 100], [50, 100], [50, 0]]
    rec_color = [ "yellow" for i in range(0, 16) ]
    rec_color_code = [ 2 for i in range(0, 16) ]
    turn = 0
    tick = 0
    turn = 0
    count = 0
    card = [0, 0]
    card_index = [0, 0]
    random.shuffle(list_1)
    label.set_text(str(turn))


def draw(canvas):
    global rec
    for i in range(0, 4):
        for j in range(0 , 4):
            
            
            rec[0] = [50 * j, 100 * i]
            rec[1] = [50 * j, 100 * (i + 1)]
            rec[2] = [50 * (j + 1), 100 * (i + 1)]
            rec[3] = [50 * (j + 1), 100 * i]  
            if rec_color_code[ i * 4 + j ] <= 1:
                canvas.draw_polygon( rec, 1, rec_color[ i * 4 + j ], rec_color[ i * 4 + j ])
            canvas.draw_text(str(list_1[ i * 4 + j ]), [(10 + 50 * j), 80 + 100 * i], 60, "cyan")
            if not exposed[ i * 4 + j ]:
                canvas.draw_polygon( rec, 1, rec_color[ i * 4 + j ], rec_color[ i * 4 + j ])
    for i in range(1, 4):
        canvas.draw_line([50 * i, 0], [50 * i, 400], 2, "black")
    for i in range(1, 4):
        canvas.draw_line([0, 100 * i], [200, 100 * i], 2, "black")
    
def click(pos):
    global exposed, tick, card, card_index, turn, label, rec_color_code, count
    for i in range(0, 4):
        for j in range(0, 4):
            if (pos[0] < (50 * (j + 1)) and pos[0] > 50 * j) and (pos[1] < (100 * (i + 1))and pos[1] > 100 * i):

                    if tick == 0:
                        if exposed[ i * 4 + j ] != True:
                            exposed[ i * 4 + j ] = True
                            card[tick] = list_1[ i * 4 + j ]
                            card_index[tick] = i * 4 + j
                            tick += 1
                    elif tick == 1:  
                        if exposed[ i * 4 + j ] != True:
                            exposed[ i * 4 + j ] = True
                            card[tick] = list_1[ i * 4 + j ]
                            card_index[tick] = i * 4 + j
                            tick += 1
                            if card[0] == card[1]:   
                                rec_color_code[ card_index[0] ] = 1
                                rec_color_code[ card_index[1] ] = 1 
                            if card[0] != card[1]:   
                                rec_color_code[ card_index[0] ] = 0
                                rec_color_code[ card_index[1] ] = 0
                                count = 0
                            turn += 1
                            label.set_text(str(turn))
                    elif tick == 2:                        
                        if card[0] != card[1]:
                            exposed[ card_index[0]] = False
                            exposed[ card_index[1]] = False
                              
                        tick = 0
                        card = [0, 0]
                        card_index = [0, 0]
                        if exposed[ i * 4 + j ] != True:
                            exposed[ i * 4 + j ] = True
                            card[tick] = list_1[ i * 4 + j ]
                            card_index[tick] = i * 4 + j
                            tick += 1

def run():
    global rec_color, rec_color_code, count
    for i in range(0, 4):
        for j in range(0, 4):
            if rec_color_code[ i * 4 + j ] == 0 and count < 2:
                rec_color[ i * 4 + j ] = "red"
            elif rec_color_code[ i * 4 + j ] == 0 and count >= 2:
                rec_color_code[ i * 4 + j ] = 2
            elif rec_color_code[ i * 4 + j ] == 1:
                rec_color[ i * 4 + j ] = "green"
            else:
                rec_color[ i * 4 + j ] = "yellow"
                rec_color_code[ i * 4 + j ] = 2
    count += 1
        
   
    
                        
                        
frame = simplegui.create_frame("Memory", 200, 400)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.add_button("New Game", new_game, 150)
frame.add_label("Turns")
label = frame.add_label(str(turn))
timer = simplegui.create_timer(100, run)


frame.start()
timer.start()