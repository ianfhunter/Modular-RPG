import random
from . import  Creature
import yaml

class MonsterFactory():

    def __init__(self):
        pass

    def produce(self, args, rand=False):
        if rand:
            import os, sys
            print(os.getcwd())
            with open("../data/creatures.yml","r") as stream:
                try:
                    data = yaml.load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
                    quit()

            idx = random.choice(list(data.keys()))
            selected_name = {"name":idx}
            origin = {"pos_X":0,"pos_Y":0,"pos_Z":0}
            stats =  {"health": 100}
            selected_name.update(origin)
            selected_name.update(stats)
            selected_monster = Creature.Creature(selected_name)
        else:
            selected_monster = Creature.Creature(args)

        return selected_monster
