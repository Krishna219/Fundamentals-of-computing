import simplegui

frame_size = [200, 200]
image_size = [1521, 1818]

def draw(canvas):
    canvas.draw_image(image,[image_size[0] / 2, image_size[1] / 2], image_size,[frame_size[0] / 2, frame_size[1] / 2],frame_size)

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

frame.start()