# implementation of card game - Memory
import simplegui, random

# load media files
aperture = simplegui.load_image("https://dl.dropbox.com/s/q73dzoit2og80e4/aperture.jpg?dl=1")
card_back = simplegui.load_image("https://dl.dropbox.com/s/l8f2b0cj7ircn22/unicorn.png?dl=1")
card_face = simplegui.load_image("https://dl.dropbox.com/s/7as58omcoebry5p/card_face2.png?dl=1")
header = simplegui.load_image("https://dl.dropbox.com/s/jxyh3thi9xymmij/memory_game_header2.png?dl=1")
gradients = simplegui.load_image("https://dl.dropbox.com/s/kgulpmeg122j6vs/rainbow_gradients.png?dl=1")
sound_on = simplegui.load_image("https://dl.dropbox.com/s/i3lljisdr9rzkko/button_on2.jpg?dl=1")
sound_off = simplegui.load_image("https://dl.dropbox.com/s/hg0ziyzpsgf4pn0/button_off2.jpg?dl=1")
reset_down = simplegui.load_image("https://dl.dropbox.com/s/fcf5fe9hp5wa4fo/reset_down.jpg?dl=1")

flip_sound = simplegui.load_sound("https://dl.dropbox.com/s/b4id9qiwoaeg9t5/card_flip.mp3?dl=1")
win_sound = simplegui.load_sound("https://dl.dropbox.com/s/kj7d609cgoxfkwx/victory_fanfare.mp3?dl=1")
shuffle_sound = simplegui.load_sound("https://dl.dropbox.com/s/xd241ygpkrb8uk6/shuffling-cards-4.mp3?dl=1")
button_sound = simplegui.load_sound("https://dl.dropbox.com/s/1anwpmiwqcf87if/click.wav?dl=1")

#  initialize globals.
flip_sound.set_volume(0.5); win_sound.set_volume(0.5)
CARD_WIDTH, CARD_HEIGHT = 50, 75
CANVAS_WIDTH, CANVAS_HEIGHT = 535, 600
CARD_Y = [150, 250, 350, 450]
BUTTON_X, BUTTON_Y, BUTTON_SIZE, BUTTON_R = 500, 565, 40, 15
GRADIENT_Y = 30
gradient_x = 0
RST_BTN_X, RST_BTN_Y = 35, 565
Y_POS = 65
win = True
sound_button = sound_off
reset_button = sound_off
sounds = False
alpha = 25
grid = [[125, 150], [205, 150], [285, 150], [365, 150], [125, 250], [205, 250], [285, 250], [365, 250], [125, 350], [205, 350], [285, 350], [365, 350], [125, 450], [205, 450], [285, 450], [365, 450]]
cards, exposed = [n%8 for n in range(16)], [False for n in range(16)]
first_card, second_card = True, False
attempts = state = 0
button_sound.set_volume(0.5)

# Banner messages. First is reserved for play prompt. List can be added to by inserting additional strings.
messages = ["M A T C H     P A I R S    T O    W I N",
            "Y O U'R E   A   W I N N E R",
            "W E L L   D O N E",
            "W A Y   T O   G O !",
            "O U T S T A N D I N G",
            "Y O U   R O C K !",
            "B R I L L I A N T !",
            "Y O U   W O N",
            "A W E S O M E",
            "F A N T A S T I Q U E",
            "F A N T A S T I S C H",
            "S U B A R A S H I I",
            "M A G N I F I C O",
            "O N G E L O O F L I J K !"]

banner = messages[1]

# helpers
def reset():
    ''' Set vars as required for new game. '''
    global exposed, first_click, second_click, state, attempts, alpha, win, reset_button
    second_click = first_click = win = True
    state = attempts = 0
    alpha = 50
    label.set_text("Turns = "+str(attempts))
    exposed = [False for n in range(16)] # populate with value False
    reset_button = sound_off
        
def new_game():
    ''' Prepare a new game. '''
    global cards, banner
    reset()
    if sounds:
        shuffle_sound.play()
    random.shuffle(cards)  
    banner = messages[0]
    

def update_banner():
    ''' Handle transparent pulsing banner message'''
    global alpha, win, banner
    alpha = (alpha + 0.2) % 75 # update alpha value for banner message.
    if False not in exposed:
        if win:
            if sounds:
                win_sound.play() # play victory sound
            win = False
            banner = messages[random.randrange(1,len(messages))] # select winner message for banner exclude first
 
            
def point_distance(x0, y0, x1, y1):
    return ( (x0 - x1)**2 + (y0 - y1)**2 )**0.5
            
            
def draw_background_elements(canvas):
    global alpha, win, gradient_x
    
    if header.get_width():	# don't draw gradient unless header has loaded
        canvas.draw_image(gradients, (CANVAS_WIDTH, 20), (CANVAS_WIDTH * 2, 40), (gradient_x, 28), (CANVAS_WIDTH * 2, 40))
    gradient_x = (gradient_x + 2) % CANVAS_WIDTH
    # Draw Header.
    canvas.draw_image(header, (535 / 2, 60), (535, 120), (535 / 2, 60), (535, 120))        
    # draw pulsing screen banner message.
    canvas.draw_text(banner,[CANVAS_WIDTH / 2 - (frame.get_canvas_textwidth(banner, 30, "sans-serif")/ 2), 126], 30, "rgba(255, 255, 255, %f)"%(1-alpha*0.01), "sans-serif")   
    # draw score aperture and text
    canvas.draw_image(aperture,(150, 60), (300, 120), (270, 565), (200, 80))     
    canvas.draw_text("turns", [195, 570], 14, "rgba(255, 255, 255, 0.5)", "sans-serif" )
    canvas.draw_text(str(attempts),[ 302 - (frame.get_canvas_textwidth(str(attempts), 40, "sans-serif")), 580], 40, "rgba(0, 0, 0, 0.5)", "sans-serif")
    # Buttons
    
    canvas.draw_image(reset_button, (BUTTON_SIZE / 2, BUTTON_SIZE / 2), (BUTTON_SIZE, BUTTON_SIZE),
                                    (RST_BTN_X, RST_BTN_Y), (BUTTON_SIZE, BUTTON_SIZE))
    canvas.draw_text("reset", [RST_BTN_X + BUTTON_SIZE / 2, RST_BTN_Y + 5], 14, "rgba(255, 255, 255, 0.5)", "sans-serif" )    
    canvas.draw_image(sound_button, (BUTTON_SIZE / 2, BUTTON_SIZE / 2), (BUTTON_SIZE, BUTTON_SIZE),
                                    (BUTTON_X, BUTTON_Y), (BUTTON_SIZE, BUTTON_SIZE))
    canvas.draw_text("sounds", [BUTTON_X - BUTTON_SIZE - 25, BUTTON_Y + 5], 14, "rgba(255, 255, 255, 0.5)", "sans-serif" )

    
# event handlers
def mouseclick(pos):
    ''' Step through game states, handle clicks, 
        update exposed card list, check for pairs. '''    
    global first_card, second_card, state, attempts, sounds, sound_button, reset_button
    clicked = None # Use none to exclude clicks outside of cards.
    for p in grid: # Check if click is inside a card rectangle mapped on the canvas
        if ( pos[0] >= p[0] and pos[0] <= p[0]+50 ) and (pos[1] >= p[1] and pos[1] <= p[1]+75):
            clicked = grid.index(p)
            
    if clicked != None:        
        if state == 0 and exposed[clicked] == False :
            exposed[clicked] = True
            if sounds:
                flip_sound.rewind(); flip_sound.play()
            first_card = clicked
            state = 1
            
        elif state == 1 and exposed[clicked] == False :
            exposed[clicked] = True
            if sounds:
                flip_sound.rewind(); flip_sound.play()
            second_card = clicked
            state = 2
            attempts += 1
            label.set_text("Turns = "+str(attempts))
            
        elif state == 2:
            if exposed[clicked] == False:
                if  not cards[first_card] == cards[second_card]:
                    exposed[first_card] = exposed[second_card] = False
                    
                if exposed[clicked] == False:
                    exposed[clicked] = True
                    if sounds:
                        flip_sound.rewind(); flip_sound.play() # preceed with rewind in case cards clicked rapidly in succession
                    first_card = clicked
                    state = 1
                    
    # Toggle sounds on / off                
    if point_distance(BUTTON_X, BUTTON_Y, pos[0], pos[1]) <= BUTTON_R:               
        if not sounds:
            button_sound.rewind(); button_sound.play()
            sound_button = sound_on
            sounds = True
        elif sounds:
            sound_button = sound_off
            sounds = False
            
    # Handle reset button on canvas
    if point_distance(RST_BTN_X, RST_BTN_Y, pos[0], pos[1]) <= BUTTON_R:               
        if  sounds:
            button_sound.play()
        reset_button = reset_down
        new_game()       
                        
def draw(canvas):
    ''' Draw screen elements '''
    global alpha, win, grid
    draw_background_elements(canvas)    
    # draw cards
    card_num = 0
    for v_pos in CARD_Y:
        card_pos = 150
        for i in range(4): # draw card face images in background.
            canvas.draw_image(card_face, (35, 47), (70, 95), (card_pos, v_pos + 37), (70, 95) )
            card_pos += 80
            
        card_pos = 150    
        for i in range(4):
            if exposed[card_num]: # Where card is revealed draw card number.
                canvas.draw_text(str(cards[card_num]),(card_pos -16, v_pos + 64), 78, "rgba(0, 0, 0, 0.5)") # Simulate drop shadow.
                canvas.draw_text(str(cards[card_num]),(card_pos -17, v_pos + 62), 72, "rgb(200, 0, 0)")
                
            elif card_back.get_width(): # Display card back image if loaded
                canvas.draw_image(card_back, (25, 38), (50, 75), (card_pos, v_pos+37), (50, 75) )    
            
            else: # Card image wasn't available so draw rectangle as card back.
                canvas.draw_polygon([[card_pos - 25, v_pos], [card_pos + 25, v_pos],
                                     [card_pos + 25, v_pos + 74],
                                     [card_pos - 25, v_pos + 74]],1, "Red", "#1d5c97")
            card_pos += 80
            card_num += 1
    update_banner()
       
                        
# create frame, add a button and labels
frame = simplegui.create_frame("Memory Game - Unicorns & Rainbows Edition   ", CANVAS_WIDTH, CANVAS_HEIGHT)
for l in range(6):
    frame.add_label("")
frame.add_button("Reset", new_game)
for l in range(3):
    frame.add_label("")
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
frame.set_canvas_background("indigo")

# Let's go
new_game()
frame.start()
#EOF