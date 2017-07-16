from Room import *
from Smelter import *
from Forge import *
from Kitchen import *
from RoomEnums import *
from Monster import *

class RoomManager():

    def __init__(self, h, w):
        self.build_map(h, w)
        self.exit_terms = ["Q","Escape"]


    def build_map(self,h,w):
        """
        [ ][ ][ ][ ][ ]
        [ ][F][L][ ][ ]
        [ ][K][S][ ][ ]
        [ ][ ][G][ ][ ]
        [ ][ ][ ][ ][ ]

        """
        self.grid = [[Room("", room_type=RoomType.Untraversable) for x in range(w)] for y in range(h)] 
        self.grid[2][2] = Smelter("Hog Goblin's Smelter")
        self.grid[1][1] = Forge("The King's Sword")
        self.grid[2][3] = Room("Garden of Harmony", room_type=RoomType.Garden)
        self.grid[2][1] = Room("Giant's Larder", room_type=RoomType.Storage, items=[Item("Key")])
        self.grid[1][2] = Kitchen("Dirty Kitchen", inhabitants=[Monster("Rabbit")])
        self.maxY = h
        self.maxX = w

    def placePlayer(self, player, xy):
        x, y = xy
        if self.grid[x][y] == 0:
            return False
        else:
            self.grid[x][y].enter(player)
            return self.grid[x][y]

    def showExits(self, xy):
        x,y = xy
        exits = {'N':False, 'E': False, 'W':False, 'S':False}
        if y - 1 != 0 and self.grid[x][y - 1].room_type != RoomType.Untraversable:
            print("To The North: "+ self.grid[x][y - 1].room_type.name)
            exits['N'] = True
        if y + 1 != self.maxY and self.grid[x][y + 1].room_type != RoomType.Untraversable:
            print("To The South: "+ self.grid[x][y + 1].room_type.name)
            exits['S'] = True
        if x - 1 != 0 and self.grid[x - 1][y].room_type != RoomType.Untraversable:
            print("To The West: "+ self.grid[x - 1][y].room_type.name)
            exits['W'] = True
        if x + 1 != self.maxX and self.grid[x + 1][y].room_type != RoomType.Untraversable:
            print("To The East: "+ self.grid[x + 1][y].room_type.name)
            exits['E'] = True
        print("You can also remain here.")
        return exits

    def chooseExits(self, available_exits, xy, player):
        selection = self.get_choice()
        if selection == -1:    
            self.leave()
        return self.parse_directions(selection, xy, available_exits, player)


    def clear(self):
        #TODO: Move to UI
        import os
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def query_direction(self):
        print("Where do you want to go?")


    def get_choice(self):
        inp = raw_input(">")
        if inp.title() in self.exit_terms:
            return -1
        else:
            return inp

    def parse_directions(self, selection, curr_coords, exits,player):
        x,y = curr_coords
        selection = selection.replace("Make","")
        selection = selection.strip()
        selection = selection.title()
        self.clear()
        if selection in ["Return", "Remain", "Stay"]:
            self.grid[x][y].enter(player)
            return curr_coords
        elif selection == "North" and exits['N']:
            print("You Travel North")
            self.grid[x][y-1].enter(player)
            return (x,y-1)
        elif selection == "East" and exits['E']:
            print("You Travel East")
            self.grid[x-1][y].enter(player)
            return (x-1,y)
        elif selection == "South" and exits['S']:
            print("You Travel South")
            self.grid[x][y+1].enter(player)
            return (x,y+1)
        elif selection == "West" and exits['W']:
            print("You Travel West")
            self.grid[x+1][y].enter(player)
            return (x+1,y)
        else:
            print("You cannot go that way.")
            return curr_coords

    def leave(self):
        quit()