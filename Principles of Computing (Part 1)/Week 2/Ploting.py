import simpleplot
import math

double = [ (x_val, 2 * x_val) for x_val in range(5)]
square = [ (x_val, math.pow(x_val, 2)) for x_val in range(5)]

#print double
#print square
#print math.pi
#
#print math.exp(1), math.floor(math.sin(math.pi)), math.cos(math.pi)
#
#print math.pow(math.e, 1)
#

x_val = []
for deg in range(0, 360, 4):
    radians = (deg) * math.pi / 180
    x_val.append(radians)
    
circle_coord = [ ((math.cos(x)), (math.sin(x))) for x in x_val ]

#print circle_coord

simpleplot.plot_lines("A plot of circle", 300, 400,
                "x", "f(x)",[circle_coord], True, ["circle"]) 
