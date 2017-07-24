import sys
sys.path.append("util")
sys.path.append("enviroment")
sys.path.append("player")
from FileIO import *
from player import *
from Smelter import *
from RoomManager import *
from pprint import pprint

player = Player()
player.inventory.add("Tin", "material", 3)
player.inventory.add("Copper", "material", 2)


rm = RoomManager(5,5)
current_coordinate = (2,2)
rm.placePlayer(player,current_coordinate)

while(1):
    rm.query_direction()
    available_exits = rm.showExits(current_coordinate)
    current_coordinate = rm.chooseExits(available_exits, current_coordinate, player)