# source of randomness is not really important here, so I'll just use Python's default.
import random
from sklearn.tree import DecisionTreeClassifier
import json
import pandas as pd

def argmax(narr): # avoids loading numpy only for this method
    arr = narr[0]
    imx = 0
    mx = -1e9
    for i, v in enumerate(arr):
        if v >= mx:
            mx = v
            imx = i
    return imx


def traverse(tree, root, ans, feature_names, class_names):
  left = tree.children_left[root]
  right = tree.children_right[root]

  leaf = (left == -1)

  ans[root] = {
      "id": root,
      "type": "leaf" if leaf else "internal",
  }

  if leaf:
    ans[root].update({
      "class": str(class_names[argmax(tree.value[root])]),
    })
  else:
    ans[root].update({
      "feature_name": str(feature_names[tree.feature[root]]),
      "feature_index": int(tree.feature[root]),
      "threshold": float(tree.threshold[root]),
      "id_left": int(left),
      "id_right": int(right)
    })
    traverse(tree, int(left), ans, feature_names, class_names)
    traverse(tree, int(right), ans, feature_names, class_names)

def tree_to_dict(feature_names, feature_types, class_names, positive_class, dt):
  ans = {
      "feature_names": list(map(str, feature_names)),
      "feature_types": list(map(str, feature_types)),
      "class_names": list(map(str, class_names)),
      "positive": str(positive_class),
      "nodes": {}
      }
  traverse(dt.tree_, 0, ans["nodes"], feature_names, class_names)
  return ans

def random_boolean_instance(dimension):
    return [random.randint(0, 1) for _ in range(dimension)]


def generate_random_dataset(n_samples, dimension, force_label=None):
    X = [random_boolean_instance(dimension) for sample in range(n_samples)]
    if force_label is None:
        y = random_boolean_instance(n_samples)
    else:
        y = [force_label for _ in range(n_samples)]
    return X, y


def generate_random_dt(dimension, n_leaves, dataset):
    dt = DecisionTreeClassifier(max_leaf_nodes=n_leaves, random_state=0)
    X, y = dataset
    dt.fit(X, y)

    ft_names = [f'ft{i}' for i in range(dimension)]
    ft_types = ['boolean' for _ in range(dimension)]
    class_names = ['positive', 'negative']
    dt_dict = tree_to_dict(ft_names, ft_types, class_names, dt)
    # check that numbr of actual leaves is not too different from specified
    n_actual_leaves = len(
        list(filter(lambda x: x['type'] == 'leaf', dt_dict['nodes'].values())))
    if n_actual_leaves < n_leaves // 2:
        print(f"n_actual_leaves = {n_actual_leaves}, n_leaves = {n_leaves}")
    return json.dumps(dt_dict, indent=2)

def dt_to_file(dimension, dt, filename, desired_n_leaves, positive_class=1):
    ft_names = [f'ft{i}' for i in range(dimension)]
    ft_types = ['boolean' for _ in range(dimension)]
    dt_dict = tree_to_dict(ft_names, ft_types, dt.classes_, positive_class, dt)
    # check that numbr of actual leaves is not too different from specified
    n_actual_leaves = len(
        list(filter(lambda x: x['type'] == 'leaf', dt_dict['nodes'].values())))
    print(f"n_actual_leaves = {n_actual_leaves}, desired_n_leaves = {desired_n_leaves}")
    with open(filename, 'w') as f:
        f.write(json.dumps(dt_dict, indent=2))

def random_dt_file(filename, dimension, n_leaves, n_samples=1000):
    dataset = generate_random_dataset(n_samples, dimension)
    with open(filename, 'w') as f:
        f.write(generate_random_dt(dimension, n_leaves, dataset))

