
from . import  WorldObject

class Creature(WorldObject.WorldObject):

    def __init__(self, args):
        super().__init__(args)
        self.health = args["health"]
        self.max_health = self.health

    def isAlive(self):
        return self.health != 0

    def isDead(self):
        return not self.isAlive()

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0: self.health = 0


    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health: self.health = self.max_health

    def isAtMaxHealth(self):
        return self.health == self.max_health
