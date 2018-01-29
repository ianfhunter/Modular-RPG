import random

class Container():
    def __init__(self, init_array):
        """
        A container is used to store things. An obvious container is a box.
        However, this class is more abstractly used to allow monsters to have item drops.
        """
        self.contents = init_array

    # Inquisitive

    def list_contents(self):
        return self.contents

    def lookup_random(self):
        return random.choice(self.contents)


    # Destructive
    def add(self, item):
        self.contents.append(item)

    def remove(self, item):
        if item in self.contents:
            return None
        self.contents.remove(item)
        return item

    def get_random_item(self):
        if len(self.contents) == 0:
            return None 
        choice = random.choice(self.contents)
        self.contents.remove(choice)
        return choice

