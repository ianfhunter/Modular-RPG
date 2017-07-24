from FileIO import *

items = load_yml("../data/items.yml",'items')

def get_many_by_type(term, requires_being_craftable=False):
    result = {}

    for x in items:
        if term == items[x]["type"]:
            if requires_being_craftable:
                if "recipe" in items[x]:
                    result.update({x:items[x]})
            else:
                result.update({x:items[x]})

    return result