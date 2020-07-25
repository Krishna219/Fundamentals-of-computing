import simplegui

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")

source_center = [220, 100]
source_size = [100, 100]
frame_size = list(source_size)
frame_center = [ source_size[0] / 2, source_size[1] /2 ]

def draw(canvas):
    canvas.draw_image( image,
                      source_center, source_size,
                      frame_center, frame_size)





frame = simplegui.create_frame("Image", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)


frame.start()

print frame_size, frame_center, source_size, source_center

