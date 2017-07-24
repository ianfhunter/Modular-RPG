from Monster import *

class Room():
    def __init__(self, name, room_type=None, inhabitants=[], items=[]):
        self.name = name
        self.room_type = room_type
        self.exit_terms = ["Exit","Leave","Depart","Quit","Q"]
        self.option_start = "*   "
        self.npcs = []
        self.monsters = []

        for x in inhabitants:
            if x.__class__.__name__ == "Monster":
                print("A MOSNTER!")
                self.monsters.append(x)

    def welcome(self):
        print "You are in the " + self.name

    def goodbye(self):
        print "You depart from the " + self.name

    def enter(self, player):
        self.welcome()

    def leave(self):
        self.clear()
        self.goodbye()

    def display_option_header(self):
        print "Available Options:"

    def display_general_room_options(self):
        print(self.option_start + "Exit")
 
    def get_choice(self):
        inp = raw_input(">")
        if inp.title() in self.exit_terms:
            return -1
        else:
            return inp

    def clear(self):
        #TODO: Move to UI
        import os
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def display_npcs(self):
        print("Noone is here")

    def display_monsters(self):
        for imp in self.monsters:
            print("There is a "+ imp.name+ " in the room.")

    def display_combat_screen(self, player):
        first_move = False
        areMonstersAlive = [ imp.isAlive() for imp in self.monsters]
        while player.isAlive() and any(areMonstersAlive):
            areMonstersAlive = [ imp.isAlive() for imp in self.monsters]
            print("Steel yourself!")
            for x in self.monsters:
                x.display(player, first_move=first_move)
            first_move = True
            player.display_health()
            player.attack_dialog(self.monsters)
        if player.isAlive():
            print("The monsters fall into pieces around you and you leave.")
            self.monsters = []
        else:
            print("Goodnight sweet warrior")
            Quit()
