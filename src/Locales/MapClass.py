import pyglet 
from Blocks.Ore import Ore


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
        [0,Ore("Tin"),2,0,0,0,0],
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

    def containObject(self, obj, pixel_yx, grid_yx):
        self.contents.append((obj, pixel_yx[1], pixel_yx[0]))
        obj.owner = self
        obj.b_y = grid_yx[0]
        obj.b_x = grid_yx[1]