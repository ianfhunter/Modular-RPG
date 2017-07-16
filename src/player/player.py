from inventory import *
from EquipmentManager import *

class Player:

    def __init__(self):
        self.health = 100
        self.inventory = Inventory(100)
        self.equipped = EquipmentManager()


    def take_damage(self, amount):
        print("You reel backwards. -"+str(amount)+"Health")
        self.health -= amount

    def isAlive(self):
        return self.health > 0

    def attack_dialog(self, opponents):
        if len(opponents) < 1:
            print("No targets")
            quit()

        invalid_action = True
        while invalid_action:
            print("Available options:")
            print("Cast Magic")
            print("Strike with weapon")
            option = self.get_choice()
            if option == "Cast":
                att = 10
            elif option == "Strike":
                att = 8
            else:
                print("invalid option")
                continue

            print("At Which Opponent? [Number only]")
            for idx, x in enumerate(opponents):
                print(str(idx) + ": "+x.name)
            which = self.get_choice()
            if int(which) < 0 or int(which) > len(opponents) -1:
                print("Invalid choice")
                continue
            else:
                self.clear()
                self.attack(att, opponents[int(which)])
                invalid_action = False

    def attack(self, damage, target):
        target.take_damage(damage)

    def get_choice(self):
        inp = raw_input(">")
        return inp

    def display_health(self):
        print("Remaining Health: "+str(self.health))

    def clear(self):
        #TODO: Move to UI
        import os
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')