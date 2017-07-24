import pyglet




class MapObject:
    def __init__(self, x, y, image):        
        self.x = x;
        self.y = y;
        self.b_x = 0;
        self.b_y = 0;
        self.img = pyglet.resource.image(image).get_texture(rectangle=True)
        self.owner = None

    def canMove(self, x, y, base_x, base_y, debug=True):
        if self.owner is None:
            return
        else:
            x_grid, y_grid = self.getAbsXY()
            if debug:
                print "Move to Position (X):" , x_grid ,"Limitation 0-"+str(len(self.owner.grid[0]))
                print "Move to Position (Y):" , y_grid ,"Limitation 0-"+str(len(self.owner.grid))
            if y_grid >= len(self.owner.grid) or y_grid < 0:        return False # Y-Dim Edge
            if x_grid >= len(self.owner.grid[0]) or x_grid < 0:     return False # X-Dim Edge
                
            if self.owner.grid[y_grid][x_grid] == 1:                return False # Untraversable
            if self.owner.grid[y_grid][x_grid] == 0:                return True  # Fallthrough Ok

    def getAbsXY(self):
        x_grid = self.b_x+self.x - 1
        y_grid = self.b_y-self.y + 1
        return (x_grid, y_grid)