import pyglet
from Utils.movement import isometric

class Interactive:

    def interact(self):
        print("Do something.")


    def prompt(self):
        self.W = pyglet.resource.image("sprites/W.png").get_texture(rectangle=True)
        self.A = pyglet.resource.image("sprites/A.png").get_texture(rectangle=True)
        self.S = pyglet.resource.image("sprites/S.png").get_texture(rectangle=True)
        self.D = pyglet.resource.image("sprites/D.png").get_texture(rectangle=True)
        print("Press S to do this thing.")
