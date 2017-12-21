class WorldObject:

    def __init__(self, args):
        self.name = args["name"]
        self.worldPosition = (args["pos_X"], args["pos_Y"], args["pos_Z"])
