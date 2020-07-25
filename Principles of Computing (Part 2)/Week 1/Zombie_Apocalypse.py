"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        #make all the cells passable using poc_grid.Grid clear() method
        poc_grid.Grid.clear(self)
        
        #reinitialise zombie and human list
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        
        #make all fields unvisited intially
        visited = [[EMPTY for dummy_i in range(self._grid_width)] for dummy_j in range(self._grid_height)]
               
        #initialise distance field with product of height times width
        distance_field = [[self._grid_width * self._grid_height for dummy_i in range(self._grid_width)] for dummy_j in range(self._grid_height)]
        
#        for entry in visited:
#            print entry
#        for entry in distance_field:
#            print entry
            
        #get the entity list
        if entity_type == HUMAN:
            entity_list = list(self._human_list)
        elif entity_type == ZOMBIE:
            entity_list = list(self._zombie_list)
        
        #create a queue with the entity list
        boundary = poc_queue.Queue()
        
        #make cells in entity list visted and distance field to zero
        for entity in entity_list:
            boundary.enqueue(entity)
            visited[entity[0]][entity[1]] = FULL
            distance_field[entity[0]][entity[1]] = 0
            

#        print boundary
#        for entry in visited:
#            print entry
#        for entry in distance_field:
#            print entry
        
        #compute distance field by breadth first search method
        #iterate till the boundary is empty
        while len(boundary):
            
            current_cell = boundary.dequeue()
            neighbors = poc_grid.Grid.four_neighbors(self, current_cell[0], current_cell[1])
            
#            print "boundary		:" + str(boundary)
#            print "current_cell	:" + str(current_cell)
#            print "neighbors	:" + str(neighbors)
#            print 
            
            for neighbor in neighbors:
                if not visited[neighbor[0]][neighbor[1]] and self.is_empty(neighbor[0], neighbor[1]):
                    visited[neighbor[0]][neighbor[1]] = FULL
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]] + 1
                    boundary.enqueue(neighbor)
                    
#                print "meighbor	:" + str(neighbor)
#                for entry in visited:
#                    print entry
#                for entry in distance_field:
#                    print entry
#                print
            
            
#        for row in range(self._grid_height):
#            for col in range(self._grid_width):
#                distance = min([(abs(entity[0] - row) + abs(entity[1] - col)) for entity in entity_list])
#                distance_field[row][col] = distance

        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        #new position for humans        
        move_list = []
        
        #for every human in human list update their position
        for human in self._human_list:
                      
            #get eight neighbors since diagonal moves are allowed
            neighbors = poc_grid.Grid.eight_neighbors(self, human[0], human[1])
                                  
            #get zombie distance for every neighbor cell
            neighbor_distance = [zombie_distance_field[neighbor[0]][neighbor[1]] if self.is_empty(neighbor[0], neighbor[1]) else EMPTY for neighbor in neighbors]
            
#            print "human			:" + str(human)
#            print "neighbors		:" + str(neighbors)
#            print "neighbor_distance	:" + str(neighbor_distance)
            
            #check if the maximum dstance is not zero 
            if max(neighbor_distance):
                
                #find the cell that has maximum distance from zombie
                max_distance_cell = neighbors[neighbor_distance.index(max(neighbor_distance))]
#                print "max_distance_cell	:" + str(max_distance_cell)

            else:
                #if the maximum dstance is zero then stay in current position
                max_distance_cell = human
                
            
            #update the new position as the largest distance cell
            move_list.append(max_distance_cell)
#            print move_list
        
        #update the position
        self._human_list = list(move_list)
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        #new position for zombies        
        move_list = []
        
        #for every zombie in zombie list update their position
        for zombie in self._zombie_list:
            
            #get four neighbors since diagonal moves are not allowed
            neighbors = poc_grid.Grid.four_neighbors(self, zombie[0], zombie[1])

            #get human distance for every neighbor cell
            neighbor_distance = [human_distance_field[neighbor[0]][neighbor[1]] for neighbor in neighbors]

#            print "zombie			:" + str(zombie)
#            print "neighbors		:" + str(neighbors)
#            print "neighbor_distance	:" + str(neighbor_distance)
#            print "currentcell_distance	:" + str(human_distance_field[zombie[0]][zombie[1]])
                                                
            #check if the current cell distance is non zero not maximum
            if human_distance_field[zombie[0]][zombie[1]] and human_distance_field[zombie[0]][zombie[1]] != self._grid_width * self._grid_height:
                
                #find the cell that has minimum distance from human
                min_distance_cell = neighbors[neighbor_distance.index(min(neighbor_distance))]
#                print "min_distance_cell	:" + str(min_distance_cell)                
            
            else:
            
                #if the current cell distance is zero then stay in current position
                min_distance_cell = zombie
                
            #update the new position as the largest distance cell
            move_list.append(min_distance_cell)
#            print move_list
        
        #update the position
        self._zombie_list = list(move_list)

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Apocalypse(30, 40))
