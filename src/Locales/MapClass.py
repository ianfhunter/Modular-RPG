import pyglet 

class MapClass:

    def __init__(self, texture="maps/room1_DEBUG.png"):
        self.grid = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [1,0,0,0,0,0,2],
        [1,0,0,0,0,0,2],
        [1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [0,0,0,0,0,0,1],
        [0,0,0,0,0,0,2],
        [0,0,0,0,0,0,2],
        [0,0,0,0,0,0,0],
        [0,2,2,0,0,0,0],
        ]
        self.x_grid_stride = 70
        self.y_grid_stride = 40
        self.texture = texture
        self.img = pyglet.resource.image(self.texture).get_texture(rectangle=True)

        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.contents = []                  # Stored as Object, X, Y

    def blit(self, window):
        self.img.blit(window.width // 2, window.height // 2, 0)
        for x in self.contents:
            x[0].blit(x[1], x[2], self.x_grid_stride, self.y_grid_stride)

    def containObject(self, obj, base_x, base_y, base_g):
        self.contents.append((obj, base_x, base_y))
        obj.owner = self
        obj.b_x = base_g[1]
        obj.b_y = base_g[0]

    def checkForPotentialInteractions(self):
        for x in self.contents:
            X, Y = x[0].getAbsXY()
            print("Currently Standing at", Y, X)
            print("Check",Y+1, X )
            if Y+1 < len(self.grid):
                if self.grid[Y+1][X] > 1:
                    print("There is an interactive object to the player's South")
            print("Check",Y-1, X)  
            if Y-1 > 0: 
                if self.grid[Y-1][X]  > 1:
                    print("There is an interactive object to the player's North")
            print("Check",Y, X+1)   
            if X+1 < len(self.grid[0]):
                if self.grid[Y][X+1]  > 1:
                    print("There is an interactive object to the player's East", "(",Y,X+1,")")
            print("Check",Y, X-1)
            if X-1 > 0:
                if self.grid[Y][X-1]  > 1:
                    print("There is an interactive object to the player's West")