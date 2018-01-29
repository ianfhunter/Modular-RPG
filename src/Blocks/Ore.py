import pyglet
from pyglet.window import key
import sys
sys.path.append('..')
from Utils.movement import isometric
from Locales.MapObject import MapObject
from Locales.InteractiveObject import Interactive


class Ore(MapObject, Interactive):
    def __init__(self, material):
        MapObject.__init__(self, None)


    def prompt(self):
        Interactive.prompt(self)