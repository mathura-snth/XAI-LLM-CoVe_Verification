import json

class DecisionTree:
    def __init__(self, root, dim):
        self.root = root
        self.dim = dim

    def get_dim(self):
        return self.dim

    def print(self):
        print(str(self.root))

    def eval(self, instance):
        assert len(instance) == self.dim
        return self.root.eval(instance)

class DTNode:
    def __init__(self, label, left, right, threshold):
        self.label = label
        self.left = left
        self.right = right
        self.threshold = threshold

    def is_leaf(self):
        return self.label in ['True', 'False']

    def eval(self, instance):
        if self.is_leaf():
            return self.label == 'True'
        if instance[self.label]:
            return self.right.eval(instance)
        else:
            return self.left.eval(instance)

    def __str__(self):
        if self.is_leaf():
            return str(self.label)
        return f"({self.label}, {str(self.left)}, {str(self.right)})"

def dict_to_DTNode(node_dict, pos_class, id_root):
    if node_dict[id_root]['type'] == 'leaf':
        label  = 'True' if node_dict[id_root]['class'] == pos_class  else 'False'
        return DTNode(label, None, None, None)
    else:
        label = node_dict[id_root]['feature_index']
        id_left = str(node_dict[id_root]['id_left'])
        id_right = str(node_dict[id_root]['id_right'])
        return DTNode(label, 
                dict_to_DTNode(node_dict, pos_class, id_left), 
                dict_to_DTNode(node_dict, pos_class, id_right),
                node_dict[id_root]['threshold'])

def parse_dt(filename):
    dt_dict = None
    with open(filename, 'r') as file:
        dt_dict = json.loads(file.read())
    dim = len(dt_dict['feature_names'])
    nodes = dt_dict['nodes']
    pos_class = dt_dict['positive']
    root = dict_to_DTNode(nodes, pos_class, '0')
    return DecisionTree(root, dim)

