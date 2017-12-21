
import unittest
import sys, os
up1 = os.path.abspath('..')
sys.path.insert(0, up1)
from modules.objs import MonsterFactory



#
#
#

#
# print(A.health)
#
# assert(A.isDead() and not A.isAlive())
#
# print("Try to loot")
#
#

# print("healed: ", A.health)

mf = None
monster = None

def gen_cactus_monster(health=100):
    origin = {"pos_X":0,"pos_Y":0,"pos_Z":0}
    mon = {"name":"Cactus Turtle"}
    stats =  {"health": health}
    mon.update(stats)
    mon.update(origin)
    A = mf.produce(mon)
    return A


class TestStringMethods(unittest.TestCase):

    def test_set_monster_creation(self):
        A = gen_cactus_monster()
        self.assertEqual(A.name, "Cactus Turtle", "Monster Generated incorrectly")

    def test_random_monster_creation(self):
        # A = mf.produce(mon, rand=True)
        # print(A.name)
        pass

    def test_health(self):
        A = gen_cactus_monster(health=200)
        self.assertEqual(A.health, 200)
        self.assertTrue(A.isAlive())
        self.assertFalse(A.isDead())

        while(A.isAlive()):
            A.take_damage(1)

        self.assertEqual(A.health, 0)
        self.assertFalse(A.isAlive())
        self.assertTrue(A.isDead())

        while(A.isDead() or not A.isAtMaxHealth()):
            A.heal(10)
        self.assertEqual(A.health, 200)
        self.assertTrue(A.isAlive())
        self.assertFalse(A.isDead())


        while(A.isAlive()):
            A.take_damage(10000)

        self.assertEqual(A.health, 0)
        self.assertFalse(A.isAlive())
        self.assertTrue(A.isDead())

    def test_harvest(self):
        A = gen_cactus_monster(health=200)
        
        while(A.isAlive()):
            A.take_damage(1)



    def setUp(self):
        global mf
        mf = MonsterFactory.MonsterFactory()


if __name__ == '__main__':
    unittest.main()
