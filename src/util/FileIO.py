import yaml

def yaml_include(loader, node):
    with file(node.value) as inputfile:
        return yaml.load(inputfile)

yaml.add_constructor("!include", yaml_include)


def load_yml(path, name):
    with open(path, 'r') as f:
        yml = yaml.load(f)
    combined_yml = {}
    for x in yml[name]:
        combined_yml.update(x)
    return combined_yml

def load_yml_simple(path, name):
    with open(path, 'r') as f:
        yml = yaml.load(f)
    combined_yml = yml[name]
    return combined_yml
