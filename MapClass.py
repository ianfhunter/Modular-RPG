import pyglet 

class MapClass:

    def __init__(self):
        self.grid = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [0,0,0,0,0,0,1],
        [0,0,0,0,0,0,1],
        [0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0],
        ]
        self.x_grid_stride = 70
        self.y_grid_stride = 40
        self.texture = "resources/maps/room1_DEBUG.png"
        self.img = pyglet.resource.image(self.texture).get_texture(rectangle=True)

        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.contents = []

    def blit(self, window):
        self.img.blit(window.width // 2, window.height // 2, 0)
        for x in self.contents:
            x[0].blit(x[1], x[2], self.x_grid_stride, self.y_grid_stride)

    def containObject(self, obj, base_x, base_y, base_g):
        self.contents.append((obj, base_x, base_y))
        obj.owner = self
        obj.b_x = base_g[1]
        obj.b_y = base_g[0]
