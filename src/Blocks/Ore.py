import pyglet
from pyglet.window import key
import sys
sys.path.append('..')
from Utils.movement import isometric
from Locales.MapObject import MapObject


class Ore(MapObject):
    def __init__(self, material):
        MapObject.__init__(self, None)

    def interact(self):
        print("Mine Ore")