
from . import  WorldObject
from . import  Container

class Creature(WorldObject.WorldObject):
    """
    A Creature is something that lives, can interact with the world and be interacted with.
    A dead creature is still a creature.
    """

    def __init__(self, args):
        super().__init__(args)
        self.health = args["health"]
        self.natural_resource = Container.Container(args["resources"])
        self.inventory = Container.Container(args["inventory"])
        self.max_health = self.health

    def isAlive(self):
        return self.health != 0

    def isDead(self):
        return not self.isAlive()

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0: self.health = 0

    def harvest(self):
        return self.natural_resource.get_random_item()


    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health: self.health = self.max_health

    def isAtMaxHealth(self):
        return self.health == self.max_health
