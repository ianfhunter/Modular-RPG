from Room import *
import sys
sys.path.append("../util")
from FileIO import *
import Resources 
sys.path.append("player")
from craft import *
from RoomEnums import *

class Kitchen(Room):
    def __init__(self, name, inhabitants):
        if name is "" :
            name = "Kitchen"
        Room.__init__(self, name, RoomType.Kitchen, inhabitants=inhabitants)
        # self.craft_list = Resources.get_many_by_type('Food', requires_being_craftable=True)

    def enter(self, player):
        Room.clear(self)
        Room.enter(self, player)

        exited = False

        Room.display_monsters(self)


        while not exited:

            exited = self.room_options(player)
            


    def room_options(self, player):
        Room.display_option_header(self)

        Room.display_combat_screen(self, player)

        return True

    def parse_options(self, selection, player):
        selection = selection.replace("Craft","")
        selection = selection.replace("Smelt","")
        selection = selection.replace("Make","")
        selection = selection.strip()
        selection = selection.title()
        Room.clear(self)
        if selection in self.craft_list.keys():
            craft(self.craft_list, selection, player.inventory)
            return True
        else:
            return False