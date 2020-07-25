import random

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = [random_point() for player in players]
    print points  
    return points

starting_points([1,2,3,4,5])