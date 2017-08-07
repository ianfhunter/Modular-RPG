import pyglet
from Utils.movement import isometric

class MapObject:
    def __init__(self, x, y, image):        
        self.x = x;
        self.y = y;
        self.b_x = 0;
        self.b_y = 0;
        if image:
            self.img = pyglet.resource.image(image).get_texture(rectangle=True)
        else:
            self.img  = None
        self.owner = None

    def canMove(self, x, y, debug=True):
        if self.owner is None:
            return False # Not inside an object, so can't move around in it.
        else:
            x_grid, y_grid = self.getAbsXY()
            print("xgrid", x_grid, "ygrid", y_grid, "x",x,"y",y)
            new_x = x_grid+x
            new_y = y_grid-y
            if debug:
                print(new_x, "=", new_y)
                print "Move to Position (X):" , new_x,"Limitation 0-"+str(len(self.owner.grid[0])-1)
                print "Move to Position (Y):" , new_y ,"Limitation 0-"+str(len(self.owner.grid)-1)
            if new_y >= len(self.owner.grid) or new_y < 0:        return False # Y-Dim Edge
            if new_x >= len(self.owner.grid[0]) or new_x < 0:     return False # X-Dim Edge
                
            if self.owner.grid[new_y][new_x] == 1:                return False # Untraversable
            if self.owner.grid[new_y][new_x] == 0:                return True  # Fallthrough Ok

    def getAbsXY(self):
        print(self.b_x, self.x)
        print(self.b_y, self.y)
        x_grid = self.b_x+self.x - 1
        y_grid = self.b_y-self.y + 1
        print(x_grid, y_grid)
        return (x_grid, y_grid)


    def move(self, x, y):
        print "Move", x, y
        if not self.canMove(x, y):
            return
        else:
            self.x, self.y = self.x + x, self.y + y


    def blit(self, base_x, base_y, MOVE_UNIT_X, MOVE_UNIT_Y):
        xy = isometric(self.x, self.y, MOVE_UNIT_X, MOVE_UNIT_Y)
        if self.img is not None:
            self.img.blit(base_x + xy[0], base_y + xy[1], 0)
