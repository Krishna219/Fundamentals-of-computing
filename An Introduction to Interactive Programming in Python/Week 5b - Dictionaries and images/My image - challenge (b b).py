#import module
import simplegui

#load image
image = simplegui.load_image("http://i.imgur.com/8piLj9m.png")

#image dimensions width * height in pixels
IMAGE_WIDTH = image.get_width()
IMAGE_HEIGHT = image.get_height()
SCALE = 2
FRAME_WIDTH = IMAGE_WIDTH / SCALE
FRAME_HEIGHT = IMAGE_HEIGHT / SCALE

#draw image constants
IMAGE_SIZE = [IMAGE_WIDTH, IMAGE_HEIGHT]
IMAGE_CENTER = [IMAGE_WIDTH / 2, IMAGE_HEIGHT / 2]
FRAME_SIZE = [FRAME_WIDTH, FRAME_HEIGHT]
FRAME_CENTER = [FRAME_WIDTH / 2, FRAME_HEIGHT / 2]
MAG_IMAGE_SIZE = [100, 100]
mag_image_center = [0, 0]
mag_frame_center = [0, 0]

#even handlers
def draw(canvas):
    if IMAGE_WIDTH > 0 and IMAGE_HEIGHT > 0:
        canvas.draw_image( image,
                          IMAGE_CENTER, IMAGE_SIZE,
                          FRAME_CENTER, FRAME_SIZE)
        canvas.draw_image( image,
                          mag_image_center, MAG_IMAGE_SIZE,
                          mag_frame_center, MAG_IMAGE_SIZE)
                          
def click(pos):
    global mag_image_center, mag_frame_center
    mag_frame_center = list(pos)
    mag_image_center[0] = mag_frame_center[0] * SCALE
    mag_image_center[1] = mag_frame_center[1] * SCALE


#create frame
frame = simplegui.create_frame("My Image", FRAME_WIDTH, FRAME_HEIGHT)

#register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

#start frame
frame.start()
