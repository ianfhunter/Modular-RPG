import pyglet
from pyglet.window import key
from utils import *
from MapObject import *

class Player(MapObject):
    def __init__(self, x,y):
        MapObject.__init__(self, x, y, "resources/sprites/man.png")

    def move(self, x, y):
        print "Move", x, y
        if not self.canMove(self.x + x, self.y+y, self.b_x, self.b_y):
            return
        self.x, self.y = self.x + x, self.y + y

    def blit(self, base_x, base_y, MOVE_UNIT_X, MOVE_UNIT_Y):
        xy = isometric(self.x, self.y, MOVE_UNIT_X, MOVE_UNIT_Y)
        self.img.blit(base_x + xy[0], base_y + xy[1], 0)

    def parseKeys(self, symbol, modifiers):
        print('A key was pressed')
        if symbol == key.LEFT:
            print("Left")
            self.move(-1,0)
        if symbol == key.RIGHT:
            print("Right")
            self.move(1,0)
        if symbol == key.DOWN:
            print("Down")
            self.move(0,-1)
        if symbol == key.UP:
            print("Up")
            self.move(0,1)