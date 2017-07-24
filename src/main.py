from __future__ import print_function
import sys

import pyglet
from pyglet.gl import *
from pyglet.window import key

from Characters.player import Player
from Locales.MapClass import MapClass

pyglet.resource.path = ['C:\\Users\\Ian\\Code\\RPGv2\\resources']
pyglet.resource.reindex()

window = pyglet.window.Window(visible=False, resizable=True)
player = Player(1,1)
smithy = MapClass()
smithy.containObject(player, 115, 215, (6, 0))
    
@window.event
def on_draw():
    window.clear()
    smithy.blit(window)

@window.event
def on_key_press(symbol, modifiers):
    player.parseKeys(symbol, modifiers)
    smithy.checkForPotentialInteractions()

if __name__ == '__main__':
    # Enable alpha blending, required for image.blit.
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    window.width = smithy.img.width
    window.height = smithy.img.height
    window.set_visible()

    pyglet.app.run()
