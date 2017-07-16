from Room import *
import sys
sys.path.append("../util")
from FileIO import *
import Resources 
sys.path.append("player")
from craft import *
from RoomEnums import *

class Smelter(Room):
    def __init__(self, name):
        if name is "" :
            name = "Smelter"
        Room.__init__(self, name, RoomType.Smelter)
        self.craft_list = Resources.get_many_by_type('Metal', requires_being_craftable=True)

    def enter(self, player):
        Room.clear(self)
        Room.enter(self, player)

        exited = False
        while not exited:

            player.inventory.display()
            exited = self.room_options(player)
            


    def room_options(self, player):
        Room.display_option_header(self)

        for x in self.craft_list:
            print(self.option_start + "Craft "  + str(x) + " (" +  str(self.craft_list[x]["recipe"]) +  ")")

        Room.display_general_room_options(self)

        selection = Room.get_choice(self)
        if selection == -1:    
            Room.leave(self)
            return True

        selection = self.parse_options(selection, player)

        if selection is False:
            print("Invalid Selection")
            return False 
        else:
            return False

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