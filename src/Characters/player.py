import pyglet
from pyglet.window import key
import sys
sys.path.append('..')
from Locales.MapObject import MapObject

class Player(MapObject):
    def __init__(self):
        MapObject.__init__(self, "sprites/man.png")

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

    def checkForPotentialInteractions(self):
        for x in self.owner.contents:
            X, Y = x[0].getAbsXY()
            print("Currently Standing at", Y, X)
            print("Check",Y+1, X )
            if Y+1 < len(self.owner.grid):
                if self.owner.grid[Y+1][X] > 1:
                    print("There is an interactive object to the player's South")
            if Y+1 < len(self.owner.grid):
                if type(self.owner.grid[Y+1][X]) != int:
                    print("There is an interactive object to the player's South 1")
                    item = self.owner.grid[Y+1][X]
            print("Check",Y-1, X)  
            if Y-1 > 0: 
                if self.owner.grid[Y-1][X]  > 1:
                    print("There is an interactive object to the player's North")
            print("Check",Y, X+1)   
            if X+1 < len(self.owner.grid[0]):
                if self.owner.grid[Y][X+1]  > 1:
                    print("There is an interactive object to the player's East", "(",Y,X+1,")")
            print("Check",Y, X-1)
            if X-1 > 0:
                if self.owner.grid[Y][X-1]  > 1:
                    print("There is an interactive object to the player's West")