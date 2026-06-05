import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import math
from pysat.card import *


def f(c):
    if c < 0 : return 0
    else : return 1 
    
def CNF_s(X, k): # Unary coding for S_i, where S_i = sum_i^j X_j,   1 < j < n
    
    S = np.zeros((len(X), len(X)))
    S_v = (np.arange(n*k)+n+1).reshape(n,k)
    a = 0
    
    for i in np.arange(0, len(X)):
        S[i,] = S[i-1,]
        if (f(X[i]) == 1):
            S[i,a] = 1
            a = a + 1

    return (S[:,0:k], S_v) # Binary coding


"""



On considère des entiers X et k tels que n = len(X) et n≥2 et k∈[1,n−1], les autres cas étant évidemment triviaux. La démarche
qui mène à définir l’encodage proposé dans cette section s’apparente à la démarche qui mène à l’encodage séquentiel proposé
par Carsten Sinz. En effet, dans l’article précité, l’auteur définit les sommes partielles S_i=∑x_j ,  0<j<n+1 et considère 
le j_ième bit s_i,j de la représentation unaire de si. Il transpose alors ces bits en variable booléenne dans un 
encodage CNF pour aboutir à l’encodage ci-dessous pour la contrainte de cardinalité ≤k(x1,...,xn).

"""


# Encoding 1 (Carsten Sinz)
    
def CNF_card(X, k): # X a list of variables X[x_1, x_2, ......, x_n], x_i in {-i,i} with i between 0 and len(X)-1 , k cardinality constraints, k in [1, n-1] (Carsten Sinz)
    
    n = len(X) # number of variables
    S = (np.arange(n*(k))+n+1).reshape(n,k)
    if k == n-1:
        L = [[-x for x in X]] # L list of clauses
    else :
        L = [[int(S[0,0]), -X[0]]] # (¬x_1 ∨ s_{1,1})
    
        for j in np.arange(1,k):
            L.append([int(-S[0,j])]) # (¬s_{1,j})
    
        for i in np.arange(1, n-1):
            L.append([-X[i], int(S[i,0])]) # (¬x_i ∨ s_{i,1})
            L.append([int(-S[i-1,0]), int(S[i,0])]) # (¬s_{i−1,1} ∨ s_{i,1})
            
            for j in np.arange(1, k):
                L.append([-X[i], int(-S[i-1,j-1]), int(S[i,j])]) # (¬x_i ∨ ¬s_{i−1,j−1} ∨ s_{i,j})
                L.append([int(-S[i-1,j]), int(S[i,j])]) # (¬s_{i−1,j} ∨ s_{i,j})
            
            L.append([-X[i], int(-S[i-1,k-1])]) # (¬x_i ∨ ¬s_{i−1,k})

        L.append([-X[n-1], int(-S[n-2,k-1])]) # (¬x_n ∨ ¬s_{n−1,k})
    
    print("Number of clauses is 2*n*k+n-3*k-1:", 2*n*k+n-3*k-1)
    print("length of L is :", len(L))
    
    return L # CNF 'Seq U^n_{<=k}'

def my_CNF_card(X, k): # X a list of variables X[x_1, x_2, ......, x_n], x_i in {-i,i} with i between 0 and len(X)-1 , k cardinality constraints, k in [1, n-1] (Carsten Sinz)

    n = len(X) # number of variable
    X = [0]+X
    begin = n
    S = []
    S.append([0]*(n+1))
    for i in range(k) :
        S.append([0]+[j for j in range(begin+1,begin+1+n)])
        begin += n
    S = np.transpose(np.array(S))
    
    L = [[-int(X[1]), int(S[1,1])]] # L list of clauses
    
    for j in np.arange(2,k+1):
        L.append([int(-S[1,j])]) 
    
    for i in np.arange(2, n):
        
        L.append([-X[i], int(S[i,1])])
        L.append([int(-S[i-1,1]), int(S[i,1])])
        
        for j in np.arange(2, k+1):
            L.append([-X[i], int(-S[i-1,j-1]), int(S[i,j])])
            L.append([int(-S[i-1,j]), int(S[i,j])])
            
        L.append([-X[i], int(-S[i-1,k])])
        
    L.append([-int(X[-1]), int(-S[n-1,k])])
    
    return L # CNF 'Seq U^n_{<=k}'

"""

Cependant, cette transposition contient une réduction qui aboutit à une perte d’information entre la variable  s_{i,j} tel 
qu’elle est encodée dans  SeqUn≤k par rapport au bit si,j décrit précédemment. En effet, le bit  si,j  est équivalent à  
s_i ≥ j. Or l’encodage  SeqUn≤k  donne  (si≥j)⇒si,j  mais pas l’implication réciproque. Cette perte d’information est 
volontaire car elle entraine un encodage plus restreint de la contrainte ≤k(x1,...,xn). Toutefois, ce choix n’est pas 
forcément judicieux lorsque l’on considère une contrainte =k(x_1,...,x_n) ou deux contraintes  ≥k_1(x_1,...,x_n)  et  
≤k_2(x_1,...,x_n)  définissant un intervalle. L’encodage  CNF  qui suit permet d’encoder exactement l’ensemble des 
équivalences (s_{i≥j})⇐⇒s_{i,j}  pour tout  i∈[1,n]  et pour tout  j∈[1,k+1] . On appelle encodage séquentiel bidirectionnel
cet encodage et on le note  SeqUn#k.
  
  
"""

# Encoding 2 
    
def CNF_card_2(X, k): # X a list of variables X[x_1, x_2, ......, x_n], x_i in {-i,i} with i between 0 and len(X)-1, k cardinality constraints, k in [1, n-1] (Carsten Sinz)
    n = len(X) # number of variable
    S_v = (np.arange(n*(k+1))+n+1).reshape(n,k+1)
    L = [[X[0], int(-S_v[0,0])]] # L list of clauses
    
    for i in np.arange(1,n): # i in [1, n]
        L.append([X[i], int(-S_v[i,0])]) #(¬x_i ∨ s_{i,1}) 
    
    for j in np.arange(1, k+1): # j in ]1, k+1]
        L.append([int(-S_v[j-1,j])])  #(¬s_{j−1,j})
        
    for i in np.arange(1,n): # i in :]1, n]
        for j in np.arange(0, k+1): # j in [1, k+1]
            L.append([int(-S_v[i-1,j]), int(S_v[i,j])]) #(¬si−1,j ∨ si,j )
            L.append([X[i], int(S_v[i-1,j]), int(-S_v[i,j])]) #(xi ∨ si−1,j ∨ ¬si,j ) 
            
    for i in np.arange(1,n): # i in ]1, n]
        for j in np.arange(1, k+1): # i in ]1, k+1]
            L.append([int(S_v[i-1,j-1]), int(-S_v[i,j])]) #(s_{i−1,j−1} ∨ ¬s_{i,j} )
            L.append([-X[i], int(-S_v[i-1,j-1]), int(S_v[i,j])]) #(¬x_i ∨ ¬s_{i−1,j−1} ∨ s_{i,j})
            
    print("number of clauses is :", len(L)) 
    return L

"""

À partir de cet encodage, il est très facile d’obtenir la contrainte de cardinalité  ≤k(x_1,...,x_n).  En effet,
il suffit de rajouter la clause  ¬s_{n,k+1}.De même, la contrainte  ≥k(x_1,...,x_n) s’obtient simplement par le rajout de
la clause  s_{n,k} . Enfin, la contrainte  =k(x_1,...,x_n) s’obtient par le rajout de 
ces deux clauses.   
    
"""
# Encoding 3 (Carsten sinz with Pysat)


def Card_pysat(X,k):
    cnf = CardEnc.atmost(lits=X, bound=k, encoding=EncType.seqcounter) # X a list of variables X[x_1, x_2, ......, x_n]
    L = cnf.clauses
    print("number of clauses (X_1) is", len(X_1))
    return L

"""

La classe CardEnc est responsable de la création de contraintes de cardinalité codées à une formule CNF.
La classe dispose de quelques méthodes de classe pour créer des contraintes parmi eux Carten sinz.
Compte tenu d’une liste de littérals, d’un entier lié et d’un type d’encodage, chacune de ces méthodes renvoie un objet de 
classe pysat.formula.CNFPlus représentant la formule CNF résultante."""


# Use the parallel counter encoding to compute the sum.
# Towards an optimal cnf encoding of boolean cardinality
# constraints –Carsten Sinz — 2005 — In Proc. of the 11th
# Intl. Conf. on Principles and Practice of Constraint Programming
# (CP 2005)

def bin(n,k):
    '''
    Convert an integer n in a binary format with k bits
    
    Parameters :
        n : int; number to encode
        k : int; number of bits available
        
    Returns :
        A list of 0 and 1 correponding to the encoding; The element number 0 is the strongest bit
    '''
    num_bits = 0   
    q = -1
    res = []
    while q != 0 and num_bits < k:
        q = n // 2
        r = n % 2
        res.append(r)
        n = q
        num_bits += 1
    return (res+[0]*(k-num_bits))

def nb_bits(n):
    '''
    Say how many bits we need to encode an integer
    
    Parameters :
        n : int; number to encode
        
    Returns :
        A int which say how many bits we need
    '''  
    return int(math.log2(n)) + 1

def halfAdder(b1, b2, s, c, cls):
    '''
    Encode a half-adder circuit in CNF (without equivalence).
    
    Parameters :
        b1, bit 1
        b2, bit 2
        s, sum bit
        c, carry bit
        
    Returns :
        cls, the set of generated clauses
    '''
    cls.append([b1, -b2, s])
    cls.append([-b1, b2, s])
    cls.append([-b1, -b2, c])


def fullAdder(b1, b2, b3, s, c, cls):
    '''
    Encode a full-adder circuit in CNF (without equivalence).
    
    Parameters :
        b1 : int; bit 1
        b2 : int; bit 2
        b3 : int; bit 3
        s : int; sum bit
        c: intt; carry bit
        
    Returns :
        cls, the set of generated clauses
    '''
    assert b1 != b2 and b2 != b3
    cls.append([b1, b2, -b3, s])
    cls.append([b1, -b2, b3, s])
    cls.append([-b1, b2, b3, s])
    cls.append([-b1, -b2, -b3, s])

    cls.append([-b1, -b2, c])
    cls.append([-b1, -b3, c])
    cls.append([-b2, -b3, c])


def encodeParallelCounter(pbLits, cls, idxVar, out):
    '''
    Encode a cardinality constrait by using the totalizer encoding.
    
    Parameters :
        pbLits, the set of literal we work on
        
    Returns :
        cls, the set of generated clauses
        out, give the result in binary form (the last on is the carry plus out[0] is the lower bit, ....)
        idxVar, the last index of var (used to create additional variable)
    '''
    if(len(pbLits) == 1):
        return cls, [pbLits[0]], idxVar

    # first compute the output variable
    nbBits = int(math.log2(len(pbLits))) + 1
    out = [idxVar + i for i in range(nbBits)]
    idxVar += nbBits

    if(len(pbLits) == 2):
        halfAdder(pbLits[0], pbLits[1], out[0], out[1], cls)
    elif(len(pbLits) == 3):
        fullAdder(pbLits[0], pbLits[1], pbLits[2], out[0], out[1], cls);
    else:
        # we sum up both part
        mid = len(pbLits) // 2
        sumLeft, sumRight = pbLits[:mid], pbLits[mid:2*mid]
        resLeft, resRight = [], []

        cls, resLeft, idxVar = encodeParallelCounter(sumLeft, cls, idxVar, resLeft)
        cls, resRight, idxVar = encodeParallelCounter(sumRight, cls, idxVar, resRight)
        assert len(resRight) + 1 == len(out) and len(resLeft) + 1 == len(out)

        # we sum the result
        if(len(pbLits) % 2 != 0):
            fullAdder(pbLits[-1], resRight[0], resLeft[0], out[0], idxVar, cls)
        else:
            halfAdder(resRight[0], resLeft[0], out[0], idxVar, cls)
        idxVar += 1

        for i in range(1, len(resRight) - 1):
            fullAdder(idxVar - 1, resRight[i], resLeft[i], out[i], idxVar, cls)
            idxVar += 1

        fullAdder(idxVar - 1, resRight[-1], resLeft[-1], out[nbBits - 2], out[nbBits - 1], cls)
    return cls, out, idxVar


def encodeWeightedParallelCounter(pbLits, coeffs, cls, idxVar, out):
    '''
    Encode a cardinality constrait by using the totalizer encoding.
    
    Parameters :
        pbLits, the set of literal we work on
        coeffs, the set of coefficient associated with pbLits
        
    Returns :
        cls, the set of generated clauses
        out, give the result in binary form (the last on is the carry, out[0] is the lower bit, ....)
        idxVar, the last index of var (used to create additional variable)
    '''
    if(len(pbLits) == 1):
        if(coeffs[0] == 1):
            out.append(pbLits[0])
        else:
            # consider the binary encoding of the coefficients
            tmp = coeffs[0]
            while(tmp != 0):
                if (tmp % 2 != 0):
                    cls.append([-pbLits[0], idxVar])
                else:
                    cls.append([-pbLits[0], -idxVar])

                out.append(idxVar)
                idxVar += 1
                tmp = tmp // 2
        return cls, out, idxVar

    # first compute the output variable
    sumCoeff = 0;
    for c in coeffs:
        sumCoeff += c
        assert c != 0

    nbBits = int(math.log2(sumCoeff)) + 1;
    out = [idxVar + i for i in range(nbBits)]
    idxVar += nbBits

    # split
    mid = len(pbLits) // 2

    # we sum up both part
    resLeft, resRight = [], []
    sumLeft, sumRight = pbLits[:mid], pbLits[mid:]
    coeffLeft, coeffRight = coeffs[:mid], coeffs[mid:]

    # print("c ", sumLeft, sumRight, coeffLeft, coeffRight, out)

    cls, resLeft, idxVar = encodeWeightedParallelCounter(sumLeft, coeffLeft, cls, idxVar, resLeft)
    cls, resRight, idxVar = encodeWeightedParallelCounter(sumRight, coeffRight, cls, idxVar, resRight)

    # we allign the results
    if(len(resRight) != len(resLeft)):
        while(len(resRight) != len(resLeft)):
            if(len(resRight) < len(resLeft)):
                resRight.append(idxVar)
            else:
                resLeft.append(idxVar)

        cls += [[-idxVar]]
        idxVar += 1

    if(len(resRight) == 1 and len(resLeft) == 1):
        halfAdder(resRight[0], resLeft[0], out[0], out[1], cls)
    else:
        halfAdder(resRight[0], resLeft[0], out[0], idxVar, cls)
        idxVar += 1

        for i in range(1, len(resLeft)):
            fullAdder(idxVar - 1, resRight[i], resLeft[i], out[i], idxVar, cls)
            idxVar += 1

        if(len(out) > len(resLeft)):
            assert len(out) == len(resLeft) + 1
            cls.append([-(idxVar - 1), out[-1]])
        else:
            assert len(out) == len(resLeft)
            cls.append([-(idxVar - 1)])

    return cls, out, idxVar

def comparator(vbits, wbits):
    """
    Enforce the fact that the bit value given in parameter is less or equal than
    the bit weight given in parameter
    Parameters:
    ----------
    vbits : list[int]
        the value represented in bits we want to constraint
    wbits : list[int]
        the bound

    Returns:
    -------
    The set of constraints needed to ensure that vbits <= wbits
    """
    assert len(vbits) == len(wbits)
    if(len(wbits) == 1):
        if(wbits[0] == 0):
            return [[-vbits[0]]]
    else:
        res = comparator(vbits[:-1], wbits[:-1])

        if wbits[-1] == 0:
            res.append([-vbits[-1]])
        else:
            for l in res:
                l.append(-vbits[-1])
        return res

    return [] # the remaining case


#!/usr/bin/python3

def totalizer(clauses, lits, idxFresh, codingVars):
    """
    Return the last index it was added to encode the problem.
    """
    #print("i: ", lits, idxFresh, codingVars)
    
    if(len(lits) < 2):
        return idxFresh
    mid = len(lits) // 2

    ll = []
    lr = []
    for i in range(len(lits)):
        if i < mid:
            ll.append(lits[i])
        else:
            lr.append(lits[i])

    #print("l: ", ll, lr)

    al = []
    if len(ll) == 1:
        al.append(ll[0])
    else:
        for i in range(len(ll)):
            al.append(idxFresh)
            idxFresh += 1 

    ar = []
    if len(lr) == 1:
        ar.append(lr[0])
    else:
        for i in range(len(lr)):
            ar.append(idxFresh)
            idxFresh += 1

    #print("a: ", al, ar)
            
    i = 0
    while i <= len(al):
        j = 0
        while j <= len(ar):
            k = i + j
            
            if k > 0:
                cl = []            
                cl.append(codingVars[k-1])
                if i > 0:
                    cl.append(-al[i-1])
                if j > 0:
                    cl.append(-ar[j-1])
                clauses.append(cl)

            if k < len(codingVars):
                cl = []
                cl.append(-codingVars[k])
                if i < len(al):
                    cl.append(al[i])
                if j < len(ar):
                    cl.append(ar[j])
                clauses.append(cl)
                
            j += 1
        i += 1

    if len(ll) > 1:
        idxFresh = totalizer(clauses, ll, idxFresh, al);
    if len(lr) > 1:
        idxFresh = totalizer(clauses, lr, idxFresh, ar);

    return idxFresh


def atLeastK(clauses, lits, k, idxFresh):
    """
    This function encodes the at least k constraint
    """
    codingVars = []
    for l in lits:
        codingVars.append(idxFresh)
        idxFresh += 1

    idxFresh = totalizer(clauses, lits, idxFresh, codingVars)

    i = 0
    while i<k and i<len(codingVars):
        clauses.append([codingVars[i]])
        i +=1

    return idxFresh, clauses

def my_totalizer(lits, idxFresh, clauses) :
    S = len(lits)
    if S == 1 : # If it's a leaf
        return lits, idxFresh, clauses
    else:
        new_lits = [i for i in range(idxFresh,idxFresh+S)]
        idxFresh += S
        mid = S//2
        left_lits = lits[0:mid]
        right_lits = lits[mid::]
        
        m = S
        m1 = mid
        m2 = S - m1
        
        left_lits, idxFresh, clauses = my_totalizer(left_lits, idxFresh, clauses)
        right_lits, idxFresh, clauses = my_totalizer(right_lits, idxFresh, clauses)
        
        #To have the same index that in the paper
        left_lits.insert(0,0)
        right_lits.insert(0,0)
        new_lits.insert(0,0)
        
        #sigma = 0
        clauses.append([left_lits[1],right_lits[1],-new_lits[1]])
            
        #General case
        for sigma in range(1,m) :
            
            if sigma < m1 : #sigma = alpha and beta = 0
                clauses.append([-left_lits[sigma],new_lits[sigma]])
                clauses.append([left_lits[sigma+1],right_lits[1],-new_lits[sigma+1]])
            elif sigma > m1 : #alpha = m1 and beta < m2
                alpha = m1
                beta = sigma - alpha
                clauses.append([-left_lits[alpha],-right_lits[beta],new_lits[sigma]])
                clauses.append([right_lits[beta+1],-new_lits[sigma+1]])
            else : # sigma = m1
                clauses.append([-left_lits[sigma],new_lits[sigma]])
                clauses.append([right_lits[1],-new_lits[sigma+1]])
            
            #sigma = beta and