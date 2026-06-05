# Encoding for whether there is a sufficient reason of size <= k.
import utils
import dtree
import math
import os

def generate_encoding(tree_filename, instance, delta, k):
    dt = dtree.parse_dt(tree_filename)

    # create variables.
    dim  = dt.get_dim()
    assert len(instance) == dim

    VM = {} # mapping from variable 'names' to ints
    IVM = {} # inverse mapping to recover names from ints
    clauses = []

    # f-variables represent whether the i-th feature is taken or not for the explanation.
    for i in range(dim):
        VM[('f', i)] = len(VM) + 1
        IVM[VM[('f', i)]] = ('f', i)

    branches = []

    def get_branches(node, curr=None): 
        # get a list of the branches
        if curr is None:
            curr = []
        if node.is_leaf():
            if node.label == 'True':
                branches.append(tuple(curr + [(node, None)]))
        else:
            get_branches(node.left, curr + [(node, 0)])
            get_branches(node.right, curr + [(node, 1)])

    get_branches(dt.root)


    def branch_to_labels(branch):
        return list(map(lambda x: x[0].label, branch))

    def branch_to_path(branch):
        return list(map(lambda x: (x[0].label, x[1]), branch))


    # create for each brand a binary number for its weight
    cnt = 1
    for branch in branches:
        cnt += 1
        b_labels = branch_to_labels(branch)
        not_in_branch = []
        for i in range(dim):
            if i not in b_labels:
                not_in_branch.append(i)
        # create weight variables.
        for i in range(dim+1):
            VM[('w', branch, i)] = len(VM) + 1
            IVM[VM[('w', branch, i)]] = ('w', branch, i)
        # create ban variables
        VM[('b', branch)] = len(VM) + 1
        IVM[VM[('b', branch)]] = ('b', branch)
        # if branch incompatible with defined variables then all w_{branch, i} should be 0.
        path = branch_to_path(branch)
        for i in range(dim):
            if (i, instance[i] == 0) in path:
                # they should all be 0s.
                clauses.append([-1*VM[('f', i)], VM[('b', branch)]])                
        # c_{branch, i, j} means amongst elements 0 to i from not_in_branch exactly j are undefined.
        for i in range(len(not_in_branch)):
            for j in range(dim+1):
                VM[('c', branch, i, j)] = len(VM) + 1
                IVM[VM[('c', branch, i, j)]] = ('c', branch, i, j)

        clauses.append([-1*VM[('c', branch, 0, 0)], VM[('f', not_in_branch[0])]])
        clauses.append([VM[('c', branch, 0, 0)], -1*VM[('f', not_in_branch[0])]])
        clauses.append([-1*VM[('c', branch, 0, 1)], -1*VM[('f', not_in_branch[0])]])
        clauses.append([VM[('c', branch, 0, 1)], VM[('f', not_in_branch[0])]])
        for j in range(2, dim+1):
            clauses.append([-1*VM[('c', branch, 0, j)]])

        for i in range(1, len(not_in_branch)):
            for j in range(dim+1):
                # c_{b, i, j} <-> (c_{b, i-1, j} and i-th is defined) or (c_{b, i-1, j-1} and i-th is undefined.)
                #   ~c_{b,i,j} or (->)  (c_{b, i-1, j} or c_{b, i-1, j-1})
                #      &   (c_{b, i-1, j} or ~f[not_branch[i]])
                #      &  f[not_branch[i]] or c_{b, i-1, j-1}
                #      & TAUT  (f[[not_branch[i]] or ~f[not_branch[i]]
                clauses.append([VM[('c', branch, i, j)], -1*VM[('c', branch, i-1, j)], -1*VM[('f', not_in_branch[i])]])
                clauses.append([-1*VM[('c', branch, i, j)], VM[('c', branch, i-1, j)], -1*VM[('f', not_in_branch[i])]])
                if j > 0:
                    clauses.append([VM[('c', branch, i, j)], -1*VM[('c', branch, i-1, j-1)], VM[('f', not_in_branch[i])]])
                    clauses.append([-1*VM[('c', branch, i, j)], VM[('c', branch, i-1, j-1)], VM[('f', not_in_branch[i])]])
                if j == 0:
                    clauses.append([-1*VM[('c', branch, i, j)], VM[('f', not_in_branch[i])]])
                    clauses.append([-1*VM[('c', branch, i, j)], VM[('c', branch, i-1, j)]])

        # let variables w_{branch, dim-i} mean that exactly i elements in not_in_branch are undefined.
        for i in range(dim+1):
            clauses.append([-1*VM[('w', branch, dim-i)], VM[('c', branch, len(not_in_branch)-1, i)]])
            clauses.append([-1*VM[('w', branch, dim-i)], -1*VM[('b', branch)]])
            clauses.append([VM[('w', branch, dim-i)], VM[('b', branch)], -1*VM[('c', branch, len(not_in_branch)-1, i)]])

    # x := how many undefined variables total (no branch consideration)            
    for i in range(dim):
        for j in range(dim+1):
            VM[('x', i, j)] = len(VM) + 1
            IVM[VM[('x', i, j)]] = ('x', i, j)
 
    clauses.append([-1*VM[('x', 0, 0)], VM[('f', 0)]])
    clauses.append([VM[('x', 0, 0)], -1*VM[('f', 0)]])
    clauses.append([-1*VM[('x', 0, 1)], -1*VM[('f', 0)]])
    clauses.append([VM[('x', 0, 1)], VM[('f', 0)]])
    for j in range(2, dim+1):
        clauses.append([-1*VM[('x', 0, j)]])

    for i in range(1, dim):
        for j in range(dim+1):
            clauses.append([VM[('x', i, j)], -1*VM[('f', i)], -1*VM[('x', i-1, j)]])
            clauses.append([-1*VM[('x', i, j)], VM[('x', i-1, j)], -1*VM[('f', i)]])
            if j > 0:
                clauses.append([VM[('x', i, j)], -1*VM[('x', i-1, j-1)], VM[('f', i)]])
                clauses.append([-1*VM[('x', i, j)], VM[('x', i-1, j-1)], VM[('f', i)]])
            if j == 0:
                clauses.append([-1*VM[('x', i, j)], VM[('f', i)]])
                clauses.append([-1*VM[('x', i, j)], VM[('x', i-1, j)]])
               
    for i in range(len(branches)-1):
        for j in range(dim+1):
            VM[('s', i, j)] = len(VM) + 1
            IVM[VM[('s', i, j)]] = ('s', i, j)
            # create carry variables, one per sum.
            VM[('k', i, j)] = len(VM) + 1
            IVM[VM[('k', i, j)]] = ('k', i, j)

    assert all(map(len, clauses))
    assert all([all(clause) for clause in clauses])

    sum_clauses, index_new_variable  = utils.compute_sum([VM[('s', 0, j)] for j in range(dim+1)], 
            [VM[('k', 0, j)] for j in range(dim+1)], # carry
            [VM[('w', branches[0], j)] for j in range(dim+1)],
            [VM[('w', branches[1], j)] for j in range(dim+1)], len(VM) + 1)
    clauses.extend(sum_clauses)
    for i in range(1, len(branches)-1):
        sum_clauses, index_new_variable = utils.compute_sum([VM[('s', i, j)] for j in range(dim+1)],
                [VM[('k', i, j)] for j in range(dim+1)], # carry
                [VM[('w', branches[i+1], j)] for j in range(dim+1)],
                [VM[('s', i-1, j)] for j in range(dim+1)], index_new_variable)
        clauses.extend(sum_clauses)


    def to_binary_array(number, dim):
        ans = [0 for i in range(dim)]
        b_str = bin(number)[2:]
        for i in range(len(b_str)):
           ans[dim-1-i] = int(b_str[len(b_str)-1-i])
        return ans

    for i in range(dim+1):
        # assume the number of undefined is i.
        # then threshold  = delta*2^i
        threshold = math.ceil(delta*(2**i))
        arr_threshold = to_binary_array(threshold, dim+1)
        exceed_target_clauses, index_new_variable  = utils.greater_equal_than([VM[('s', len(branches)-2, j)] for j in range(dim+1)], arr_threshold, index_new_variable)
        for clause in exceed_target_clauses:
            clauses.append([-1*VM[('x', dim-1, i)]] + clause)

    assert all([all(clause) for clause in clauses])
    if k is not None:
        at_most_k_clauses = utils.at_most_k([VM[('f', i)] for i in range(dim)],index_new_variable, k)
        clauses.extend(at_most_k_clauses)
        return clauses
    else:
        soft_clauses = [[-1*VM[('f', i)]] for i in range(dim)]
        return clauses, soft_clauses

