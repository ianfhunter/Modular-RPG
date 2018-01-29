class WorldObject:

    def __init__(self, args):
        """
        A WorldObject is something that exists in the world. What form, plane or appearance 
        the object takes is irrellivant. As long as it can be given a precise position, it should
        inherit from this class.
        Note: Gases, Vast expanses of liquid and other tricky substances can use this class, 
        but be sure to provide some deterrants to developers asking for the exact co-ordinate of the 
        Atlantic.
        """
        self.name = args["name"]
        self.worldPosition = (args["pos_X"], args["pos_Y"], args["pos_Z"])
