import sys
sys.path.append('../src/Locales')
from MapObject import *
from MapClass import *
import unittest

class TestMovementAllowed(unittest.TestCase):

    def setUp(self):
        self.testMapObject = MapObject(0, 0, "debug.png")
        self.testMapClass = MapClass(texture="debug.png")

    def tearDown(self):
        self.testMapObject = None
        self.testMapClass = None

    def test_movement_only_if_in_room(self):
        res = self.testMapObject.canMove(-1,0)
        self.assertFalse(res)
        res = self.testMapObject.canMove(0,-1)
        self.assertFalse(res)
        res = self.testMapObject.canMove(1,0)
        self.assertFalse(res)
        res = self.testMapObject.canMove(0,1)
        self.assertFalse(res)
        res = self.testMapObject.canMove(0,0)
        self.assertFalse(res)

    def test_movement_in_object(self):
        self.testMapClass.grid = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]

        self.testMapClass.containObject(self.testMapObject,100,100,(1,1)) # Pixel, Coord

        res = self.testMapObject.canMove(1,0)
        self.assertTrue(res)
        res = self.testMapObject.canMove(0,1)
        self.assertTrue(res)
        res = self.testMapObject.canMove(-1,0)
        self.assertTrue(res)
        res = self.testMapObject.canMove(0,-1)
        self.assertTrue(res)
        res = self.testMapObject.canMove(0,0)
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()