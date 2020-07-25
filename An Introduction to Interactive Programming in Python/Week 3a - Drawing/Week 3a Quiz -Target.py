import simplegui

def draw(canvas):
    canvas.draw_circle([150,150], 145, 1, "black", "white")  
    canvas.draw_circle([150,150], 130, 1, "black", "White") 
    canvas.draw_circle([150,150], 115, 1, "gray", "black")
    canvas.draw_circle([150,150], 100, 1, "white", "black")
    canvas.draw_circle([150,150], 85, 1, "black", "cyan")  
    canvas.draw_circle([150,150], 70, 1, "black", "cyan")
    canvas.draw_circle([150,150], 55, 1, "black", "red")  
    canvas.draw_circle([150,150], 40, 1, "black", "red")
    canvas.draw_circle([150,150], 25, 1, "black", "yellow") 
    canvas.draw_circle([150,150], 15, 1, "black", "yellow")
    canvas.draw_circle([150,150], 5, 1, "black", "yellow")
   
frame = simplegui.create_frame("Quiz 3 a", 300, 300)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)
frame.start()
