def position_tile(self, tile_pos, req_pos):
    """
    Positions the given tile at the required position
    tile_pos - tile to be positioned
    req_pos - required position
    returns a move string
    """
    tot_moves = ""

    current_position = self.current_position(tile_pos[0], tile_pos[1])

    #find relative position of target tile with respect to zero tile
    relative_pos = (current_position[0] - req_pos[0], current_position[1] - req_pos[1])


    #Four cases of solving based on relative position
    if relative_pos[0] == 1: #tile lies in row below target row 
        
            move = ""
            
            #tile is in solved position move zero tile to the end of the current row
            for dummy_i in range(current_zero_position[1], self._width - 1):
                move += "r"
                
            tot_moves += move

    elif relative_pos[0] == 0: #tile lies in same row as target row
        
        if relative_pos[1] < 0: #tile lies in same row and to the left
            
            move = ""

            #move zero tile left to the target cell position
            for dummy_i in range(relative_pos[1], 0):
                move += "l"

            #move target tile right
            for dummy_i in range(relative_pos[1], -1):
                move += "urrdl"

            tot_moves += move  
            
        else:#tile lies in same row and to the right
            
            move = ""

            #move zero tile right to the target cell position
            for dummy_i in range(relative_pos[1]):
                move += "r"

            #move target tile left
            for dummy_i in range(1, relative_pos[1]):
                move += "ulldr"

            tot_moves += move 

    elif relative_pos[1] == 0:#tile lies in same col as target col

        move = ""

        #move zero tile up to the target cell position
        for dummy_i in range(relative_pos[0], 0):
            move += "u"
            
        #move target tile down
        for dummy_i in range(relative_pos[0], -1):
            move += "lddru"
        
        #move zero tile to the left of target tile
        move += "ld"        
        tot_moves += move    

    else:

        move = ""

        #move zero tile to the target cell position
        if relative_pos[1] < 0:
            for dummy_i in range(relative_pos[0], 0):
                move += "u"
            for dummy_i in range(relative_pos[1], 0):
                move += "l"

            #move target tile right
            for dummy_i in range(relative_pos[1], -1):
                if current_position[0] == 0:
                    move += "drrul"
                else:
                    move += "urrdl"

        else:
            for dummy_i in range(relative_pos[0], 0):
                move += "u"
            for dummy_i in range(relative_pos[1]):
                move += "r"

            #move target tile left                               
            for dummy_i in range(1, relative_pos[1]):
                if current_position[0] == 0:
                    move += "dllur"
                else:
                    move += "ulldr"

            #place zero tile left of target
            if current_position[0] == 0:
            move += "dllu"
            else:
            move += "ulld"

        #move target tile down
        move += "dru"

        for dummy_i in range(relative_pos[0], -1):
            move += "lddru"

        #move zero tile to the left of target tile
        move += "ld"
        tot_moves += move

    return tot_moves