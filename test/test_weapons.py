
import unittest
import sys, os
up1 = os.path.abspath('..')
sys.path.insert(0, up1)
from modules.objs import WeaponFactory
from modules.objs import ItemFactory
from test_beings import gen_cactus_monster

wf = None

def gen_magical_sword():
    origin = {"pos_X":0,"pos_Y":0,"pos_Z":0}
    weapon = {"name":"Pointy Stick"}
    stats = {"attack": 5,
             "durability": 3,
             "speed": 7}
    weapon.update(origin)
    weapon.update(stats)
    A = wf.produce(weapon)
    return A


class TestWeaponMethods(unittest.TestCase):

    def test_set_weapon_creation(self):
        weapon = gen_magical_sword()
        self.assertEqual(weapon.name, "Pointy Stick", "Weapon Generated incorrectly")

    def test_weapon_damage(self):
        mon = gen_cactus_monster(health=200)
        weapon = gen_magical_sword()

        self.assertFalse(weapon.isDestroyed())
        weapon.damage(mon)
        weapon.damage(mon)
        self.assertEqual(mon.health, 190)
        self.assertTrue(weapon.isDamaged())
        self.assertFalse(weapon.isDestroyed())
        weapon.damage(mon)
        self.assertTrue(weapon.isDestroyed())

    def test_weapon_speed(self):
        weapon = gen_magical_sword()
        weapon_2 = gen_magical_sword()

        weapon_2.improve("speed", 5)
        fastest_sword = weapon.contest(weapon_2)
        self.assertEqual(fastest_sword, weapon_2)


    def setUp(self):
        global wf
        wf = WeaponFactory.WeaponFactory()

if __name__ == '__main__':
    unittest.main()
