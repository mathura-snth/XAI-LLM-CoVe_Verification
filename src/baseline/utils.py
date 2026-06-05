def clauses_to_dimacs(clauses, filename):
    vars = set()
    for clause in clauses:
        for lit in clause:
            vars.add(abs(lit))
    n_vars = max(vars)
    n_clauses = len(clauses)

    with open(filename, 'w') as file:
        file.write(f'p cnf {n_vars} {n_clauses}\n')
        for clause in clauses:
            clause_str = ' '.join(map(str, clause)) + ' 0\n'
            file.write(clause_str)

def weighted_to_dimacs(clauses, soft_clauses, filename):
    clauses_to_dimacs(clauses, filename + '.uw')
    vars = set()
    for clause in (clauses+soft_clauses):
        for lit in clause:
            vars.add(abs(lit))

    n_vars = max(vars)
    n_clauses = len(clauses) + len(soft_clauses)

    with open(filename, 'w') as file:
        top = len(soft_clauses) + 1
        file.write(f'p wcnf {n_vars} {n_clauses} {top}\n')
        for clause in clauses:
            clause_str = ' '.join(map(str, [top] + clause)) + ' 0\n'
            file.write(clause_str)
        for clause in soft_clauses:
            clause_str = ' '.join(map(str, [1] + clause)) + ' 0\n'
            file.write(clause_str)

# use n*k encoding.
def at_most_k(variables, index_new_variables, k):
    if k >= len(variables): #trivially true.
        return []
    # index_new_variables states from what index the new variables should start.
    clauses = []
    n = len(variables)
    # a_{i,j} means that from v_0, ..., v_i, at least  j variables are true
    # with j in {0,...,k+1}.
    V = {}
    IVM = {}
    for i in range(n):
        for j in range(k+2):
            V[('a', i, j)] = index_new_variables + len(V)
            IVM[V[('a', i, j)]] = ('a', i, j)
    # we then want ~ a_{n-1, k+1}
    clauses.append([-1*V[('a', n-1, k+1)]])
    clauses.append([V[('a', 0, 0)]])
    clauses.append([-1*variables[0], V[('a', 0, 1)]])
    # propagation
    for i in range(n-1):
        for j in range(k+2):   
            # if a_{i, j} -> a_{i+1, j} 
            clauses.append([-1*V[('a', i, j)], V[('a', i+1, j)]])
            # if a_{i, j} and v[i+1] -> a_{i+1, j+1}
            if j <= k:
                clauses.append([-1*V[('a', i, j)], -1*variables[i+1],  V[('a', i+1, j+1)]])
    return clauses

def eq_lit_cl(lit, cls):
    return [[-1*lit] + cls] + [ [-1*l, lit] for l in cls]

def implies(cls_1, cls_2, index_new_variable, debug=False):
    clauses = []
    new_vars = []
    for cl_1 in cls_1:
        clauses.extend(eq_lit_cl(index_new_variable, cl_1))
        new_vars.append(index_new_variable)
        index_new_variable += 1

    for cl_2 in cls_2:
        clauses.append(cl_2 + [-1*var for var in new_vars])
    if debug: print(f'cls_1 = {cls_1}, clauses = {clauses}')
    return clauses, index_new_variable

def eq(cls_1, cls_2, index_new_variable, debug=False):
    clauses, index_new_variable = implies(cls_1, cls_2, index_new_variable, debug)
    clauses_2, index_new_variable = implies(cls_2, cls_1, index_new_variable, debug)
    return clauses+clauses_2, index_new_variable

def xor_vs(a, b, c):
    return [[a,b,c], [-a, -b, c], [a, -b, -c], [-a, b, -c]]

def at_least_2(a, b, c):
    return [[a,b], [a,c], [b,c]]

def compute_sum(rtarget, carry, rs_1, rs_2, index_new_variable, debug=False):
    target = list(reversed(rtarget))
    s_1 = list(reversed(rs_1))
    s_2 = list(reversed(rs_2))
 
    assert len(target) == len(s_1)
    assert len(target) == len(s_2)
    assert len(target) == len(carry)
    dim = len(target)
    clauses = [ [-1*target[0], -1*s_1[0], -1*s_2[0]],
                [-1*target[0], s_1[0], s_2[0]],
                [target[0], -1*s_1[0], s_2[0]],
                [target[0], s_1[0], -1*s_2[0]]] # xor s_1[-1] and s_2[-1].
    clauses.append([-1*carry[0]])
    for i in range(1, dim):
        xor_clauses = xor_vs(s_1[i], s_2[i], carry[i])
        clauses_p, index_new_variable = eq([[target[i]]], xor_clauses, index_new_variable, debug and i == 3)
        clauses.extend(clauses_p)
        clauses_t, index_new_variable = eq([[carry[i]]], at_least_2(s_1[i-1], s_2[i-1], carry[i-1]), index_new_variable)
        clauses.extend(clauses_t)
    assert all(map(len, clauses))
    assert all([all(clause) for clause in clauses])
    return clauses, index_new_variable


def greater_equal_than(vars_1, arr, index_new_variable):
    # (vars_1[0] & ~vars_2[0]) v (equals + recursive)
    assert len(vars_1) == len(arr)
    if len(vars_1) == 1:
        if arr[0] == 0:
            return [], index_new_variable
        else:
            return [[vars_1[0]]], index_new_variable
    rec_clauses, index_new_variable = greater_equal_than(vars_1[1:], arr[1:], index_new_variable)
    if arr[0] == 1:
        return  [[vars_1[0]]] + rec_clauses, index_new_variable
    else:
        return [rec_clause + [vars_1[0]] for rec_clause in rec_clauses], index_new_variable

def get_vars(vars_to_print, filename):
    M = {}
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i == 0: continue
            s = line[:-1].split(' ')[1:]
            for el in s:
                M[abs(int(el))] = int(int(el) > 0)
    return [M[v] for v in vars_to_print]



