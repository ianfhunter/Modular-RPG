
from . import  WorldObject
from . import  Item

class Weapon(Item.Item):
    """
    A weapon is strictly a thing used for inflicting harm upon another person.
    This class is only for physical items. Use a different class for things like 
    telepathic attacks, curses and the dizziness you get when you spin round and 
    round in a circle really fast. 
    """

    def __init__(self, args):
        super().__init__(args)
        self.attr = {
            "attack": args["attack"],
            "durability": args["durability"],
            "max_durability": args["durability"],
            "speed": args["speed"],
        }


    def improve(self, attribute, value):
        self.attr[attribute]+=value

    def contest(self, another_weapon):
        if self.attr["speed"] > another_weapon.attr["speed"]:
            return self
        elif self.attr["speed"] < another_weapon.attr["speed"]:
            return another_weapon
        else:
            return None


    def isDestroyed(self):
        return self.attr["durability"] == 0

    def isDamaged(self):
        return self.attr["durability"] < self.attr["max_durability"]

    def damage(self, object):
        object.take_damage(self.attr["attack"])
        self.attr["durability"]-=1
