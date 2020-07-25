"""
Merge function for 2048 game.
"""

def shift_to_front(lst):
    """
    Function that shifts all the non-zero entries of the list 'line' to the front
    Exactly shifts all the zeros to the end
    """
    for index in range(0, len(lst) - 1):
        
        #if an element is zero just swap it with the number next to it
        
        if lst[index] == 0:
            lst[index] = lst[index + 1]
            lst[index + 1] = 0
            
            #The following code checks if the swapped element is zero 
            #And ensures all the non zero entries are at the front
            #for example [0, 0, 2, 4] the result should be [2, 4, 0, 0]
            #the above code alone will give [0, 2, 4, 0] 
            
            dummy_index = index
            
            while dummy_index > 0:
                if lst[dummy_index - 1] == 0:
                    lst[dummy_index - 1] = lst[dummy_index]
                    lst[dummy_index] = 0
                dummy_index -= 1
                
    return lst
    
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    line = list(shift_to_front(list(line)))
    
    #Code to add/ merge equal adjacent cells and place the sum in the first cell
    #replacing the second cell with zero (as per order - proceeding from left to right)
    
    for index in range(0, len(line) - 1):
        if line[index] == line[index + 1]:
            line[index] += line[index + 1]
            line[index + 1] = 0
    
    line = list(shift_to_front(list(line)))
    
    return line

print merge([0, 2])
#print merge([2, 0, 2, 4])
#print merge([0, 0, 2, 2])
#print merge([2, 2, 0, 0])
#print merge([2, 2, 2, 2])
#print merge([8, 16, 16, 8])