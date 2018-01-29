
from . import  WorldObject

class Item(WorldObject.WorldObject):

    def __init__(self, args):
        """
        An item is something a creature can interact with, and pick up. sub-classes may allow
        for more advanced usage, such as equipping, activation or modification.
        While something like a door would be foolish for a human to pick up,
        a giant may wish to use it as a shield. That being said, if we introduce the option of
        playing a giant into the game, we will probably have 'bigger' problems.
        """
        super().__init__(args)
