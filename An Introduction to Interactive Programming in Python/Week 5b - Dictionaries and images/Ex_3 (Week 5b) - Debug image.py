import simplegui

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png")

image_size = [134, 164]
image_center = [ image_size[0] / 2, image_size[1] /2]


def draw(canvas):
    canvas.draw_image( image,
                      image_center, image_size,
                      image_center, image_size)





frame = simplegui.create_frame("Image", image_size[0], image_size[1])
frame.set_draw_handler(draw)


frame.start()



