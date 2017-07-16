
import sys
sys.path.append("../util")
from FileIO import *

monster_list = load_yml_simple("../data/monsters.yml",'Monsters')


class Monster():



    def __init__(self, name):
        self.name = name
        self.get_monster(self.name)

    def get_monster(self, name):
        self.health =  monster_list[self.name]["Health"]
        self.att = 1 * monster_list[self.name]["attack modifier"]


    def display(self, player, first_move=False):
        print("A hideous "+self.name+" stands in front of you.")
        if first_move:
            print("It attacks you!")
            self.attack(player)
        else:
            print("It reels back in shock. Strike Quick!")

    def attack(self, player):
        print("The creature lashes out at you. ")
        player.take_damage(self.att)

    def take_damage(self, amount):
        print("The creature shrieks in pain. -" + str(amount) + " Health")
        self.health -= amount

    def isAlive(self):
        return self.health > 0