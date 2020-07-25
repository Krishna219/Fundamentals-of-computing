class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        print self.x,self.y

    def translate(self, deltax = 0, deltay = 0):
        """Translate the point in the x direction by deltax
           and in the y direction by deltay."""
        self.x += deltax
        self.y += deltay
        print self.x,self.y
        
#point1 = Point2D(3, 9)
#point2 = Point2D()
#point2.translate(20, 4)

#point = Point2D(3, 9)
#point.translate(5, -2)

#point = Point2D(3, 9)
#translate(point, 5, -2)

point = Point2D(3, 9)
point.translate(5, -2)