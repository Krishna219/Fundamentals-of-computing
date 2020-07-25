# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
started = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
#            self.lifespan = float('inf')
            self.lifespan = False
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

boz = simplegui.load_sound("https://dl-web.dropbox.com/get/BOZ.mp3?_subject_uid=352500373&w=AABli5AA3eBMPhL8BiU63g4SJRbG1-2CHyOrop17sYaRrg")
boz.set_volume(.6)

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def process_sprite_group(group, canvas):
    for obj in set(group):
        obj.draw(canvas)
        obj.update()
        if obj.update():
#            print obj.update()
            group.remove(obj)

def group_collide(sprite_group, obj):
    global explosion_group
    for sprite in set(sprite_group):
        if sprite.collide(obj):
            explosion = Sprite(obj.get_position(), [0, 0], 0, 0, explosion_image, explosion_info, explosion_sound)
            explosion_group.add(explosion)
            sprite_group.remove(sprite)
            return True
    return False

def group_group_collide(rock_group, missile_group):
    global score
    number_of_collisions = 0
    for missile in set(missile_group):
        if group_collide(rock_group, missile):
            number_of_collisions += 1
            missile_group.remove(missile)
    return number_of_collisions

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
#        canvas.draw_circle(self.pos, self.radius, 1, "White", "White"
        if self.thrust:
            canvas.draw_image(self.image,
                          [self.image_center[0] + 90, self.image_center[1]], self.image_size,
                          self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image,
                          self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)
                          
    def update(self):
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.angle += self.angle_vel
        for i in range(2):
            self.vel[i] *= (1 - 0.03)
        forward_vector = angle_to_vector(self.angle)
        if self.thrust:
            for i in range(2):
                self.vel[i] += forward_vector[i] / 2.5
                
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos
        
    def increment_angle_vel(self):
        self.angle_vel += 0.08
    
    def decrement_angle_vel(self):
        self.angle_vel -= 0.08
        
    def reset_angle_vel(self):
        self.angle_vel = 0
       
    def set_thruster(self, thrust):
        self.thrust = thrust
    
    def shoot(self):
        global missile_group
        forward_vector = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + 45 * forward_vector[0], self.pos[1] + 45 * forward_vector[1]]
        missile_vel = [self.vel[0] + 3.5 * forward_vector[0], self.vel[1] + 3.5 * forward_vector[1]]
        missile = Sprite(missile_pos, missile_vel, 0, 0, missile_image, missile_info, missile_sound)
        missile_group.add(missile)
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos
    
    def draw(self, canvas):
#        canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        if self.animated:
            current_explosion_index = (self.age % self.lifespan) // 1
            image_center = [self.image_center[0] + current_explosion_index * self.image_size[0], self.image_center[1]]  
            canvas.draw_image(self.image,
                          image_center , self.image_size,
                          self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image,
                          self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)
        
    def update(self):
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.angle += self.angle_vel 
        if self.lifespan:
            self.age += 0.5
            if int(self.age) == self.lifespan:
                self.lifespan = False
#                print int(self.age), self.lifespan
                return True
        return False
    
    def collide(self, obj): 
        obj_radius = obj.get_radius()
        obj_pos = obj.get_position()
        if dist(self.pos, obj.pos) <= (self.radius + obj.radius):
            return True
        return False
    
#event handlers
def keydown_handler(key):
    global my_ship
    if simplegui.KEY_MAP['space'] == key:
        my_ship.shoot()
    if simplegui.KEY_MAP['up'] == key:
        my_ship.set_thruster(True)
        ship_thrust_sound.rewind()
        ship_thrust_sound.play()
    if simplegui.KEY_MAP['left'] == key:
        my_ship.decrement_angle_vel()
    elif simplegui.KEY_MAP['right'] == key:
        my_ship.increment_angle_vel()

def keyup_handler(key):
    global my_ship
    if simplegui.KEY_MAP['up'] == key:
        my_ship.set_thruster(False)
        ship_thrust_sound.pause()
    if simplegui.KEY_MAP['left'] == key or simplegui.KEY_MAP['right'] == key:
        my_ship.reset_angle_vel()

def click(pos):
    global started, lives, score
    size = splash_info.get_size()
    inwidth = pos[0] > (WIDTH - size[0]) / 2 and pos[0] < (WIDTH + size[0]) / 2 
    inheight = pos[1] > (HEIGHT - size[1]) / 2 and pos[1] < (HEIGHT + size[1]) / 2
    if not started and inwidth and inheight:
        started = True
        lives = 3
        score = 0
    
def draw(canvas):
    global time, lives, score, started
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text("Lives : " + str(lives), [50, 50], 36, "rgb(150, 155, 250)")
    canvas.draw_text("Score : " + str(score), [600, 50], 36, "rgb(150, 155, 250)")

    # draw ship and sprites
    my_ship.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    
    #groupwise operation
    process_sprite_group(rock_group, canvas)
    
    if group_collide(rock_group, my_ship):
        if lives > 0:
            lives -= 1
        if lives == 0:
            started = False
            for rock in set(rock_group):
                rock_group.pop()
            
    score += group_group_collide(rock_group, missile_group)
    
    process_sprite_group(explosion_group, canvas)
    
    process_sprite_group(missile_group, canvas)
    
    #draw starting image
    if not started:
        canvas.draw_image(splash_image,
                          splash_info.get_center(), splash_info.get_size(), 
                          [WIDTH / 2, HEIGHT / 2], splash_info.get_size())
        soundtrack.play()
        boz.pause()
        
    else:
        soundtrack.pause()
        boz.play()
            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group, started
    rock_position = [random.randrange(WIDTH), random.randrange(HEIGHT)]
    rock_velocity = [random.randrange(2), random.randrange(2)]
    rock_angle_vel = random.randrange(-30, 30) / 200.0
#    if len(rock_group) <= 1 and not started:
#        rock_group = set([Sprite(rock_position, rock_velocity, 0, rock_angle_vel, asteroid_image, asteroid_info)])
    if len(rock_group) < 12 and started:
        rock = Sprite(rock_position, rock_velocity, 0, rock_angle_vel, asteroid_image, asteroid_info)
        rock_group.add(rock)
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT, 0)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], math.pi / 2, ship_image, ship_info)

#a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.05, asteroid_image, asteroid_info
rock_group = set()
#missile_group = set([Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)])
missile_group = set()
explosion_group = set()

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000, rock_spawner)

# get things rolling
timer.start()
frame.start()
