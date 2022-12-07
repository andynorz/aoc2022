#from operator import itemgetter

class Tree:
    def __init__(self, name="/", parent=None):
        self.children = []
        self.parent = parent
        self.name = name
        self.size = 0
    def __repr__(self):
        return self.name

class File:
    def __init__(self, name=None, size=None):
        self.name = name
        self.size = size

    def __repr__(self):
        return self.name

dir_sizes = dict()

def get_node_from_name(node: Tree, name: str):
    for c in node.children:
        if c.name == name:
            return c


def get_dirsizes(root: Tree):
    root.size = sum(get_dirsizes(d) for d in root.children if type(d) == Tree)
    root.size += sum(f.size for f in root.children if type(f) == File)

    dir_sizes[root] = root.size
    return root.size


def create_tree(data):
    root = Tree()
    current_node = root
    for row in data:
        
        # It's a command
        first, *rest = row.split()
        if first == "$":
            # It's a command
            match rest[0]:
                case "cd":
                    match rest[1]:
                        case "/":
                            # Gå till root
                            current_node = root
                        case "..":
                            # Gå upp ett hack
                            current_node = current_node.parent
                        case _:
                            # Gå till önskad dir
                            current_node = get_node_from_name(current_node, rest[1])

        # It's a dir            
        elif first == "dir":
            node = Tree(name=rest[0], parent=current_node)
            current_node.children.append(node)
        # It's a file
        elif first.isnumeric():
            file = File(size=int(first), name=rest[0])
            current_node.children.append(file)

    return root


with open(r"aoc22_7_input") as f:
    data = f.readlines()

tree = create_tree(data)
total_size = get_dirsizes(tree)

free = 70_000_000 - total_size
new_needed = 30_000_000 - free
print(f"Total size: {total_size} Free: {free} Needed {new_needed}")

all_dirs = list(sorted(((k,v) for (k, v) in dir_sizes.items()), key=lambda x: x[1]))
dirs_lower_100k = list(((k,v) for (k, v) in dir_sizes.items() if v <= 100_000))
dirs_to_be_deleted = list(sorted(((k,v) for (k, v) in dir_sizes.items() if v > new_needed), key=lambda x: x[1]))
print(dirs_to_be_deleted[0])


