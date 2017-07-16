import pyglet


class MapObject:
    def __init__(self, x, y, image):        
        self.x = x;
        self.y = y;
        self.img = pyglet.resource.image(image).get_texture(rectangle=True)
        self.owner = None

    def canMove(self, x, y, base_x, base_y, debug=False):
        if self.owner is None:
            return
        else:
            y_grid = base_y-y+1
            x_grid = base_x+x-1
            if debug:
                print "Move to Position (Y):" , y_grid ,"Limitation 0-"+str(len(self.owner.grid))
                print "Move to Position (Y):" , x_grid ,"Limitation 0-"+str(len(self.owner.grid[0]))
            if y_grid >= len(self.owner.grid) or y_grid < 0:        return False # Y-Dim Edge
            if x_grid >= len(self.owner.grid[0]) or x_grid < 0:     return False # X-Dim Edge
                
            if self.owner.grid[y_grid][x_grid] == 1:                return False # Untraversable
            if self.owner.grid[y_grid][x_grid] == 0:                return True  # Fallthrough Ok