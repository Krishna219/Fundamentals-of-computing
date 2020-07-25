#modules
import simplegui
import random

#------------------------------ GLOBAL VARIABLES ------------------------------#

#one in CAPITALS are constants and donot vary throughout the program

#frame details
WIDTH = 470
HEIGHT = 510
FRAME_BACKGROUND_COLORS = [['indigo', 'teal', 'violet'],
                           ['blue', 'red', 'green', 'pink', 'violet', 'cyan', 'orange', 'maroon']]


#box details
box_size = { 3 : [140, 120], 4 : [105, 90], 5 : [84, 72]} #maps the MATRIX_SIZE with corresponding BOX_SIZE = [BOX_WIDTH, BOX_HEIGHT]


first_box_center = { 3 :[box_size[3][0] / 2 + 25, box_size[3][1] / 2 + 125],
                      4 :[box_size[4][0] / 2 + 25, box_size[4][1] / 2 + 125],
                      5 :[box_size[5][0] / 2 + 25, box_size[5][1] / 2 + 125]} #it varies depending on the size [3 X 3, 4 X 4, 5 X 5]
                      

#text details
text_height = { 3 : 45, 4 : 37, 5 : 31} #maps the MATRIX_SIZE with the corresponding TEXT_SIZE

COLOR_DIC = {0 : ["white", "white"],  #color dictionary maps the ALL POSIBBLE numbers with their respective COLORS and BOX_FILL_COLOR
             2 : ["gray", "white"],
             4 : ["maroon", "white"],
             8 : ["blue", "violet"],
            16 : ["orange", "white"],
            32 : ["blue", "cyan"],
            64 : ["red", "white"],
           128 : ["brown", "orange"],
           256 : ["black", "green"],
           512 : ["white", "red"],
          1024 : ["orange", "indigo"],
          2048 : ["lime", "maroon"],
          4096 : ["black", "lime"],
          8192 : ["blue", "yellow"],
         16384 : ["pink", "blue"]}

#matrix
matrix_size = 4

#game play details
started = False
double_click = False

score = 0

seperation_line = [[0, 50], [WIDTH, 50],
                   [0, 100], [WIDTH, 100]]


started_box = [[100, 125], [100, 225],   #the box that encloses START button
               [350, 225], [350, 125]]

boxes = { 3 :  [[[160, 250], [160, 300], #boxes dictionary map the MATRIX_SIZE with their ENCLOSING_BOX and the ENCLOSING_BOX_COLOR
               [310, 300], [310, 250]],
                "cyan"],
          4 :  [[[160, 315], [160, 365],
               [310, 365], [310, 315]],
                "cyan"],
          5 :  [[[160, 380], [160, 435],
               [310, 435], [310, 380]],
                "cyan"]}
          
started_color = "pink"
started_color_change = False

play_again_box = [[[100, 270], [100, 350],
                [350, 350], [350, 270]],
                "yellow"]

play_again_color_change = False

menu_circle_box = [[[440, 0], [440, 50],
                       [WIDTH, 50], [WIDTH, 0]],
                   "gray"]
                       
menu_box = [[[WIDTH - 100, 50], [WIDTH - 100, 100], [WIDTH, 100], [WIDTH, 50]],
            [[WIDTH - 100, 100], [WIDTH - 100, 150], [WIDTH, 150], [WIDTH, 100]]]

menu_on = False

menu_data = {1 : ['Back', [WIDTH - 90, 90], 30, 'gray'],
             2 : ['Undo', [WIDTH - 90, 140], 30, 'gray']}

#keeping track of color change (duration of change)
no_of_ticks = 0
click = 0

#------------------------------ HELPER FUNCTIONS ------------------------------#

#find the position of the number

def position(number):
    if number // 1000 != 0:
        return 2.7
    elif number // 100 != 0:
        return 3
    elif number // 10 != 0:
        return 4
    else:
        return 10

#matrix creation

def create_matrix():
    global matrix, boxes, l, score, undo_matrix 

    matrix = []
    score = 0
    l = Matrix(matrix_size)
    undo_matrix = Matrix(matrix_size)
    BOX_SIZE = box_size[matrix_size]
    FIRST_BOX_CENTER = first_box_center[matrix_size]
    TEXT_HEIGHT = text_height[matrix_size]
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            if (i == matrix_size - 1) and (j == matrix_size / 2 or j == matrix_size / 2 + 1):
                value = 2
            else:
                value = 0 #random.choice([0, 2, 4, 8, 16, 32, 64, 128, 256, 512])
            color = COLOR_DIC[value][0]
            
            box_center = [FIRST_BOX_CENTER[0] + j * BOX_SIZE[0],
                          FIRST_BOX_CENTER[1] + i * BOX_SIZE[1]]
            
            number = Number(value, box_center, BOX_SIZE, TEXT_HEIGHT, color)
            matrix.append(number)

def undo():
    global matrix, undo_matrix

    undo_matrix.set_matrix()

#controls the matrix values when left button is pressed
def left_manager():
    
    global matrix, l, score, undo_matrix

    undo_matrix.copy_matrix()
    
    l.copy_matrix()

    l.shift_left()

    l.add_left()

    l.shift_left()

    l.add_value('right')
    
    l.check()

    score = l.get_score()

    l.set_matrix()

#controls the matrix values when right button is pressed
def right_manager():
    
    global matrix, l, score, undo_matrix

    undo_matrix.copy_matrix()

    l.copy_matrix()

    l.shift_right()

    l.add_right()

    l.shift_right()

    l.add_value('left')

    l.check()

    score = l.get_score()

    l.set_matrix()

#controls the matrix values when up button is pressed
def up_manager():
    
    global matrix, l, score, undo_matrix

    undo_matrix.copy_matrix()

    l.copy_matrix()

    l.shift_up()

    l.add_up()

    l.shift_up()

    l.add_value('down')

    l.check()

    score = l.get_score()

    l.set_matrix()

#controls the matrix values when down button is pressed
def down_manager():
    
    global matrix, l, score, undo_matrix

    undo_matrix.copy_matrix()

    l.copy_matrix()

    l.shift_down()

    l.add_down()

    l.shift_down()

    l.add_value('up')

    l.check()

    score = l.get_score()

    l.set_matrix()
    
#------------------------------ OBJECTS ------------------------------#

#object that contains coordinates of respective boxes for numbers and their colors
            
class Box():
    def __init__(self, center, number, box_size, color = "gray"):
        self.center = list(center)
        self.color = color
        self.fill_color = COLOR_DIC[number][1]

        #box coordinates
        point_1 = [self.center[0] - box_size[0] / 2, self.center[1] - box_size[1] / 2]
        point_2 = [point_1[0] + box_size[0], point_1[1]]
        point_3 = [point_1[0] + box_size[0], point_1[1] + box_size[1]]
        point_4 = [point_1[0], point_1[1] + box_size[1]]
        self.points = [point_1, point_2, point_3, point_4]

    def __str__(self):
        return str(self.points) + " " + str(self.center)

    def get_coordinates(self):
        return self.points

    def update(self, value):
        self.fill_color = COLOR_DIC[value][1]

    def draw(self, canvas):
        canvas.draw_polygon(self.points, 5, self.color, self.fill_color)

#my object for holding a number with its associated color and location
        
class Number():
    def __init__(self, value, center, box_size, text_height, color):
        self.box_size = list(box_size)
        self.box_center = center
        self.text_height = text_height
        self.value = value
        self.position = [center[0] - box_size[0] / position(self.value), center[1] + box_size[1] / 4]
        self.color = color
        self.box = Box(center, self.value, self.box_size)

    def __str__(self):
        return str(self.value) + " " + str(self.position) + " " + self.color

    def get_value(self):
        return self.value

    def get_position(self):
        return self.position

    def get_color(self):
        return self.color

    def draw(self, canvas):
        self.box.draw(canvas)
        canvas.draw_text(str(self.value), self.position, self.text_height, self.color)

    def update(self, value):
        self.value = value
        self.color = COLOR_DIC[self.value][0]
        self.position = [self.box_center[0] - self.box_size[0] / position(self.value), self.box_center[1] + self.box_size[1] / 4]
        self.box.update(self.value)

#object that processes all maatrix operations shift, add, get, print

class Matrix():
    def __init__(self, matrix_size):
        self.l = []
        self.score = 0
        for i in range(matrix_size):
            sub_l = []
            for j in range(matrix_size):
                sub_l.append(0)
            self.l.append(sub_l)

    def print_matrix(self):
        for i in range(matrix_size):
            for j in range(matrix_size):
                print self.l[i][j],
            print
        print

    def get_score(self):
        return self.score  
        
    def set_matrix(self):
        for i in range(matrix_size):
            for j in range(matrix_size):
                matrix[i * matrix_size + j].update(self.l[i][j])
                    
    def copy_matrix(self):
        for i in range(matrix_size):
            for j in range(matrix_size):
                self.l[i][j] = matrix[i * matrix_size + j].get_value()

    def add_value(self, where):
        if where == 'right':
            count = 0
            j = matrix_size - 1
            for i in range(matrix_size - 1, -1, -1):
                if self.l[i][j] == 0 and count  == 0:
                    self.l[i][j] = random.choice([2, 4])
                    count += 1
                    
        elif where == 'left':
            count = 0
            j = 0
            for i in range(matrix_size - 1, -1, -1):
                if self.l[i][j] == 0 and count  == 0:
                    self.l[i][j] = random.choice([2, 4])
                    count += 1 

        elif where == 'down':
            count = 0
            i = matrix_size - 1
            for j in range(matrix_size - 1, -1, -1):
                if self.l[i][j] == 0 and count  == 0:
                    self.l[i][j] = random.choice([2, 4])
                    count += 1

        elif where == 'up':
            count = 0
            i = 0
            for j in range(matrix_size - 1, -1, -1):
                if self.l[i][j] == 0 and count  == 0:
                    self.l[i][j] = random.choice([2, 4])
                    count += 1 

    def shift_left(self):
        for j in range(matrix_size - 1):
            for i in range(matrix_size):
                if self.l[i][j] == 0:
                    self.l[i][j] = self.l[i][j + 1]
                    self.l[i][j + 1] = 0
                    k = j
                    while k > 0:
                        if self.l[i][k - 1] == 0:
                            self.l[i][k - 1] = self.l[i][k]
                            self.l[i][k] = 0
                        k -= 1

    def shift_right(self):
        for j in range(matrix_size - 1, 0, -1):
            for i in range(matrix_size):
                if self.l[i][j] == 0:
                    self.l[i][j] = self.l[i][j - 1]
                    self.l[i][j - 1] = 0
                    k = j
                    while k < matrix_size - 1:
                        if self.l[i][k + 1] == 0:
                            self.l[i][k + 1] = self.l[i][k]
                            self.l[i][k] = 0
                        k += 1
                        
    def shift_up(self):
        for i in range(matrix_size - 1):
            for j in range(matrix_size):
                if self.l[i][j] == 0:
                    self.l[i][j] = self.l[i + 1][j]
                    self.l[i + 1][j] = 0
                    k = i
                    while k > 0:
                        if self.l[k - 1][j] == 0:
                            self.l[k - 1][j] = self.l[k][j]
                            self.l[k][j] = 0
                        k -= 1

    def shift_down(self):
        for i in range(matrix_size - 1, 0, -1):
            for j in range(matrix_size):
                if self.l[i][j] == 0:
                    self.l[i][j] = self.l[i - 1][j]
                    self.l[i - 1][j] = 0
                    k = i
                    while k < matrix_size - 1:
                        if self.l[k + 1][j] == 0:
                            self.l[k + 1][j] = self.l[k][j]
                            self.l[k][j] = 0
                        k += 1
                        
    def add_left(self):
        for j in range(matrix_size - 1):
            for i in range(matrix_size):
                if self.l[i][j] == self.l[i][j + 1]:
                    self.l[i][j] += self.l[i][j + 1]
                    self.score += self.l[i][j]
                    self.l[i][j + 1] = 0

    def add_right(self):
        for j in range(matrix_size - 1, 0, -1):
            for i in range(matrix_size):
                if self.l[i][j] == self.l[i][j - 1]:
                    self.l[i][j] += self.l[i][j - 1]
                    self.score += self.l[i][j]
                    self.l[i][j - 1] = 0

    def add_up(self):
        for i in range(matrix_size - 1):
            for j in range(matrix_size):
                if self.l[i][j] == self.l[i + 1][j]:
                    self.l[i][j] += self.l[i + 1][j]
                    self.score += self.l[i][j]
                    self.l[i + 1][j] = 0

    def add_down(self):
        for i in range(matrix_size - 1, 0, -1):
            for j in range(matrix_size):
                if self.l[i][j] == self.l[i - 1][j]:
                    self.l[i][j] += self.l[i - 1][j]
                    self.score += self.l[i][j]
                    self.l[i - 1][j] = 0

    def check(self):
        global started, double_click, matrix
        count = 0
        for i in range(matrix_size):
            for j in range(matrix_size):
                if self.l[i][j] != matrix[i * matrix_size + j].get_value():
                    count += 1
        if count == 0 and started:
            started = False
            frame.set_canvas_background(random.choice(FRAME_BACKGROUND_COLORS[0]))

#------------------------------ EVENT HANDLERS ------------------------------#

#drawing on the canvas
        
def draw(canvas):
    global score,  menu_circle_box, menu_on, menu_data
    if started and double_click:
        canvas.draw_polygon([[0, 0], seperation_line[0], seperation_line[1], [WIDTH, 0]], 1, "black", "black")
        canvas.draw_polygon([seperation_line[0], seperation_line[2], seperation_line[3], seperation_line[1]], 1, "gray", "gray")
        canvas.draw_polygon(menu_circle_box[0], 1, "gray", "black")
        for i in range(3):
            canvas.draw_circle([455, 15 + i * 10], 2, 1, menu_circle_box[1], menu_circle_box[1])
        canvas.draw_text("Score : " + str(score), [25, 90], 35, "black")
        for value in matrix:
            value.draw(canvas)
        if menu_circle_box[1] == "green":
            canvas.draw_polygon(menu_box[0], 1, "green", "black")
            canvas.draw_polygon(menu_box[1], 1, "green", "black")
            canvas.draw_text(menu_data[1][0], menu_data[1][1], menu_data[1][2], menu_data[1][3])
            canvas.draw_text(menu_data[2][0], menu_data[2][1], menu_data[2][2], menu_data[2][3])
    elif double_click:
        canvas.draw_polygon([[0, 0], seperation_line[0], seperation_line[1], [WIDTH, 0]], 1, "black", "black")
        canvas.draw_polygon([seperation_line[0], seperation_line[2], seperation_line[3], seperation_line[1]], 1, "gray", "gray")
        canvas.draw_text("Score : " + str(score), [25, 90], 35, "black")
        canvas.draw_text("Game over", [110, 210], 50, "black")
        canvas.draw_polygon(play_again_box[0], 8, "orange", play_again_box[1])
        canvas.draw_text("Play again", [135, 320], 40, "indigo")        
    else:
        canvas.draw_text("2", [WIDTH / 4 + 15, HEIGHT / 4 - 30], 80, COLOR_DIC[2][0])
        canvas.draw_text("0", [WIDTH / 4 + 65, HEIGHT / 4 - 30], 80, COLOR_DIC[0][0])
        canvas.draw_text("4", [WIDTH / 4 + 115, HEIGHT / 4 - 30], 80, COLOR_DIC[4][0])
        canvas.draw_text("8", [WIDTH / 4 + 165, HEIGHT / 4 - 30], 80, COLOR_DIC[8][0])
        canvas.draw_polygon(started_box, 8, "orange", started_color)
        canvas.draw_polygon(boxes[3][0], 8, "orange", boxes[3][1])
        canvas.draw_polygon(boxes[4][0], 8, "orange", boxes[4][1])
        canvas.draw_polygon(boxes[5][0], 8, "orange", boxes[5][1])
        canvas.draw_text("Start", [WIDTH / 3, 190], 65, "black")
        canvas.draw_text("3 X 3", [WIDTH / 2.5, 290], 40, "black")
        canvas.draw_text("4 X 4", [WIDTH / 2.5, 355], 40, "black")
        canvas.draw_text("5 X 5", [WIDTH / 2.5, 420], 40, "black")

#mouse position

def mouse_click(pos):
    global started, started_color_change, play_again_color_change, double_click, click, no_of_ticks, boxes, matrix_size, menu_on, menu_box
    if not started and not double_click:
        start_pos_x = started_box[0][0] < pos[0] < started_box[2][0]
        start_pos_y = started_box[0][1] < pos[1] < started_box[2][1]
        if start_pos_x and start_pos_y:
            click += 1
            started_color_change = True
            no_of_ticks = 0
            if click == 2:
                create_matrix()
                started = True
                double_click = True
                click = 0
                frame.set_canvas_background(random.choice(FRAME_BACKGROUND_COLORS[1]))

        three_pos_x = boxes[3][0][0][0] < pos[0] < boxes[3][0][2][0]  #checking if the mouse position is within the box of 3 X 3
        three_pos_y = boxes[3][0][0][1] < pos[1] < boxes[3][0][2][1]

        four_pos_x = boxes[4][0][0][0] < pos[0] < boxes[4][0][2][0]   #checking if the mouse position is within the box of 4 X 4
        four_pos_y = boxes[4][0][0][1] < pos[1] < boxes[4][0][2][1]

        five_pos_x = boxes[5][0][0][0] < pos[0] < boxes[5][0][2][0]   #checking if the mouse position is within the box of 5 X 5
        five_pos_y = boxes[5][0][0][1] < pos[1] < boxes[5][0][2][1]
    
        if three_pos_x and three_pos_y:
            boxes[3][1] = "lime"
            boxes[4][1] = "cyan"
            boxes[5][1] = "cyan"
            matrix_size = 3
            click = 0
        
        elif four_pos_x and four_pos_y:
            boxes[3][1] = "cyan"
            boxes[4][1] = "lime"
            boxes[5][1] = "cyan"
            matrix_size = 4
            click = 0
        
        elif five_pos_x and five_pos_y:
            boxes[3][1] = "cyan"
            boxes[4][1] = "cyan"
            boxes[5][1] = "lime"
            matrix_size = 5
            click = 0
            
    elif not started and double_click:
        play_again_pos_x = play_again_box[0][0][0] < pos[0] < play_again_box[0][2][0]
        play_again_pos_y = play_again_box[0][0][1] < pos[1] < play_again_box[0][2][1]
        if play_again_pos_x and play_again_pos_y:
            click += 1
            play_again_color_change = True
            no_of_ticks = 0
            if click == 2:
                boxes[3][1] = "cyan"
                boxes[4][1] = "cyan"
                boxes[5][1] = "cyan"
                matrix_size = 4
                double_click = False
                click = 0
                frame.set_canvas_background(random.choice(FRAME_BACKGROUND_COLORS[0]))
    else:
        menu_circle_pos_x = menu_circle_box[0][0][0] < pos[0] < menu_circle_box[0][2][0]
        menu_circle_pos_y = menu_circle_box[0][0][1] < pos[1] < menu_circle_box[0][2][1]
        if menu_circle_pos_x and menu_circle_pos_y:
            click += 1
            if click % 2 != 0:
                menu_circle_box[1] = "green"
                menu_on = True
            else:
                menu_circle_box[1] = "gray"
                menu_on = False
        else:
            if menu_on:
                menu_box1_pos_x = menu_box[0][0][0] < pos[0] < menu_box[0][2][0]
                menu_box1_pos_y = menu_box[0][0][1] < pos[1] < menu_box[0][2][1]
                menu_box2_pos_x = menu_box[1][0][0] < pos[0] < menu_box[1][2][0]
                menu_box2_pos_y = menu_box[1][0][1] < pos[1] < menu_box[1][2][1]

                if menu_box1_pos_x and menu_box1_pos_y:
                    boxes[3][1] = "cyan"
                    boxes[4][1] = "cyan"
                    boxes[5][1] = "cyan"
                    matrix_size = 4
                    started = False
                    double_click = False
                    frame.set_canvas_background(random.choice(FRAME_BACKGROUND_COLORS[0]))
                elif menu_box2_pos_x and menu_box2_pos_y:
                    undo()
                    
            menu_circle_box[1] = "gray"
            menu_on = False
            click = 0
        
#timer handler

def tick():
    global started_color, started_color_change, three_color_change, no_of_ticks, play_again_box, play_again_color_change, menu_on
    
    if started_color_change and no_of_ticks <= 10:
        started_color = "lime"
    elif started_color_change and no_of_ticks > 10:
        started_color = "pink"
        started_color_change = False
        
    if play_again_color_change and no_of_ticks <= 10:
        play_again_box[1] = "lime"
    elif play_again_color_change and no_of_ticks > 10:
        play_again_box[1] = "yellow"
        play_again_color_change = False

    no_of_ticks += 1
    
#when a key is held down this function will take place

def key_down(key):
    if key == simplegui.KEY_MAP['left'] and started:
        left_manager()
    elif key == simplegui.KEY_MAP['right'] and started:
        right_manager()
    elif key == simplegui.KEY_MAP['up'] and started:
        up_manager()
    elif key == simplegui.KEY_MAP['down'] and started:
        down_manager()

#------------------------------ CREATING FRAME and FRAME ELEMENTS ------------------------------#

#creating frame
    
frame = simplegui.create_frame("2048", WIDTH, HEIGHT)
frame.set_canvas_background(random.choice(FRAME_BACKGROUND_COLORS[0]))
frame.set_mouseclick_handler(mouse_click)
frame.set_keydown_handler(key_down)
frame.set_draw_handler(draw)

#------------------------------ CREATING TIMER ------------------------------#

timer = simplegui.create_timer(100, tick)

#------------------------------ RUNNING PROGRAM ------------------------------#

#start timer
timer.start()

#open frame
frame.start()
