import pyglet




class MapObject:
    def __init__(self, x, y, image):        
        self.x = x;
        self.y = y;
        self.b_x = 0;
        self.b_y = 0;
        self.img = pyglet.resource.image(image).get_texture(rectangle=True)
        self.owner = None

    def canMove(self, x, y, debug=True):
        if self.owner is None:
            return  # Not inside an object, so can't move around in it.
        else:
            x_grid, y_grid = self.getAbsXY()
            new_x = x_grid+x
            new_y = y_grid-y
            if debug:
                print "Move to Position (X):" , new_x,"Limitation 0-"+str(len(self.owner.grid[0]))
                print "Move to Position (Y):" , new_y ,"Limitation 0-"+str(len(self.owner.grid))
            if new_y >= len(self.owner.grid) or new_y < 0:        return False # Y-Dim Edge
            if new_x >= len(self.owner.grid[0]) or new_x < 0:     return False # X-Dim Edge
                
            if self.owner.grid[new_y][new_x] == 1:                return False # Untraversable
            if self.owner.grid[new_y][new_x] == 0:                return True  # Fallthrough Ok

    def getAbsXY(self):
        x_grid = self.b_x+self.x - 1
        y_grid = self.b_y-self.y + 1
        return (x_grid, y_grid)