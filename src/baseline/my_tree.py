import os

import numpy as np
from pysat.formula import CNF
from pysat.pb import PBEnc

import encodage_CNF as enc
from pysat.formula import WCNF
from pysat.examples.rc2 import RC2
from pysat.solvers import Glucose4
import subprocess
import uuid

sign = lambda x: int(x > 0) - int(x < 0)


# creation of a binary decision tree
class decision_tree:

    def __init__(self, root=None, labels=None):
        '''
        Allow to construct a decision tree
        
        Parameters : 
            root : decision_node; The node which will be the root of the decision_tree
            labels : list : It's a list containing the name of the ith label at the ith indices
        
        Returns : A decision_tree
        '''
        self._root = root
        self.scykitTree = None
        if root != None:
            self._nb_features = root.nb_features
            self._nb_class = len(root.probabilities)
            self._l_child = root.searchChild()
            self._bina = root.hash_bin()
            impossible_inst_clauses = []
            for idx_feature in range(1, self.nb_features + 1):
                lits = []
                threshold = []
                nb = 0
                for k in self._bina.keys():
                    if k[0] == idx_feature:
                        lits.append(self._bina[k][0])
                        threshold.append((k[1], nb))
                        nb += 1
                threshold.sort(reverse=True)
                indices = [y for (x, y) in threshold]
                for i in range(len(indices) - 1):
                    impossible_inst_clauses.append([-lits[indices[i]], lits[indices[i + 1]]])
            self._threshold_clauses = impossible_inst_clauses
            if labels is None:
                self._labels = [i for i in range(len(root.probabilities))]
            else:
                if len(labels) == len(root.probabilities):
                    self._labels = labels
                else:
                    raise ValueError("labels must have the length than the array of probabilities of the root node")
        else:
            self._nb_features = None
            self._nb_class = None
            self._l_child = None
            self._bina = None
            self._threshold_clauses = None
            self._labels = None

    @property
    def root(self):
        return self._root

    @property
    def labels(self):
        return self._labels
    

    @labels.setter
    def labels(self, labels):
        if len(labels) == len(self.root.probabilities):
            self._labels = labels
        else:
            raise ValueError("labels must have the length than the array of probabilities of the root node")

    @root.setter
    def root(self, root):
        self._root = root
        self._nb_features = root.nb_features
        self._nb_class = len(root.probabilities)
        self._l_child = root.searchChild()
        self._bina = root.hash_bin()

    @property
    def bina(self):
        return self._bina

    @bina.setter
    def bina(self, bina):
        self._bina = bina

    @property
    def nb_class(self):
        return self._nb_class

    @property
    def l_child(self):
        return self._l_child

    @property
    def nb_features(self):
        return self._nb_features

    def insert_node(self, node, way):
        '''
        Add a decision_node in our decision_tree
        
        Parameters : 
            node : decision_node; The node to add to our tree
            way : list of char; This list is a list like ['r','l','r'] where 'r' means we need to follow the right child and 'l' the left child. The first char is the direction take at the root node and the last one is where we need to place it on the node studied at this moment
        '''

        if (node.nb_features == self.nb_features) and (self.nb_class == len(node.probabilities)):
            current_node = self.root
            for i in range(0, len(way) - 1):
                c = way[i]
                if c == "r" or c == "R":
                    current_node == current_node.right
                elif c == "l" or c == "L":
                    current_node == current_node.left
                else:
                    raise ValueError(f"{c} is an invalid character in way")
                if current_node == None:
                    raise TypeError(
                        "There must have an error in your selected way, current_node shouldn't be None at this step")
            c = way[-1]
            if c == "r" or c == "R":
                current_node.right = node
            elif c == "l" or c == "L":
                current_node.left = node
            else:
                raise ValueError(f"{c} is an invalid character in way")
        else:
            raise TypeError("The node added must have the same dimension of feature and of output classes")

    def insert_tree(self, tree, way):
        '''
        Add a decision_tree as a sub tree in our decision_tree
        
        Parameters :
            tree : decision_tree; The sub tree to add to our tree
             way : list of char; This list is a list like ['r','l','r'] where 'r' means we need to follow the right child and 'l' the left child. The first char is the direction take at the root node and the last one is where we need to place it on the node studied at this moment
        
        Returns:
            list of char; This list is a list like ['r','l','r'] where 'r' means we need to follow the right child and 'l' the left child. The first char is the direction take at the root node and the last one is where we need to place it on the node studied at this moment
        '''
        node = tree.root
        self.insert_node(node, way)

    def tree_to_text(self):
        '''
        Print the decision_tree structure
        '''
        node = self.root
        return node.node_to_text(0)

    def from_DecisionTreeClassifier(self, tree_scikit):
        '''
        Convert a binary decision tree of scikit in a tree decision_tree
        
        Parameters :
            tree_scikit : sklearn.tree.DecisionTreeClassifier; The tree from scikit format to encode in my_tree format
            
        Returns : decision_tree with the same structure
        '''
        ts = tree_scikit.tree_  # We take only what we need
        dico_node = {}
        binarisation = {}
        card_bin = 0
        self.scykitTree = tree_scikit
        # First, we will create all the nodes
        for i in range(len(ts.feature)):
            if ts.feature[i] >= 0:
                if binarisation.get((int(ts.feature[i] + 1), ts.threshold[i]), None) is None:
                    card_bin += 1
                    binarisation[(int(ts.feature[i] + 1), ts.threshold[i])] = [card_bin, 1]
                else:
                    binarisation[(int(ts.feature[i] + 1), ts.threshold[i])][1] += 1
                node = decision_node(tree_scikit.n_features_in_, int(ts.feature[i] + 1), ts.threshold[i], ts.value[i][0])
                dico_node[i] = node
        # Secondly, we make all links between all nodes
        for i in range(len(ts.feature)):
            parent = dico_node.get(i, None)
            if parent != None:
                left = dico_node.get(ts.children_left[i], None)
                right = dico_node.get(ts.children_right[i], None)
                if left != None:
                    dico_node[i].left = left
                else:
                    dico_node[i].left = ts.value[ts.children_left[i]][0]
                if right != None:
                    dico_node[i].right = right
                else:
                    dico_node[i].right = ts.value[ts.children_right[i]][0]
        # Finally we build the tree by pointing the node root
        if dico_node.get(0, None) is None:  # If the tree is just a leaf
            self.root = decision_node(tree_scikit.n_features_in_, 1, 0, ts.value[0][0])
            self._bina = {(1, 0): [1, 1]}
        else:
            self.root = dico_node[0]
            self._bina = binarisation
        impossible_inst_clauses = []
        for idx_feature in range(1, self.nb_features + 1):
            lits = []
            threshold = []
            nb = 0
            for k in self._bina.keys():
                if k[0] == idx_feature:
                    lits.append(self._bina[k][0])
                    threshold.append((k[1], nb))
                    nb += 1
            threshold.sort(reverse=True)
            indices = [y for (x, y) in threshold]
            for i in range(len(indices) - 1):
                impossible_inst_clauses.append([-lits[indices[i]], lits[indices[i + 1]]])
        self._threshold_clauses = impossible_inst_clauses
        self.labels = tree_scikit.classes_

    def take_decision(self, instance):
        '''
        Allow to take a decision with the tree
        
        Parameters :
            instance : numpy array corresponding to the value of the feature on each attributes
        
        Returns :
            int; int which correspond to classification of the feature
        '''
        return self.root.take_decision(instance)

    def predict(self, instance):
        '''
        Allow to take a decision with the tree
        
        Parameters :
            instance : numpy array corresponding to the value of the feature on each attributes
        
        Returns :
            The name associated to the label selected
        '''
        return self._labels[self.root.take_decision(instance)]

    def to_CNF(self, target=None, hash_bin=None, method="comp", threshold_clauses=True, aux=None):
        '''
        Return a logical proposition as CNf or a DNF which is equivalent to the tree
        
        Parameters :
            target : int; say for which label the CNF is true
            hash_bin : dict; A dict corresponding to a hashmap (num_feature, threshold) <-> (associated boolean, number of appearence) NB : You can use a dict saying only the associated boolean
            method : string; If equal to "comp", it create the CNF using the negation of the DNF which is true when we don't have the correct label. If equal to "tseytin", we made the CNF by making the corresponding DNF and then, use tseytin to convert it into a CNF
            aux : int; In the case where "tseytin" is use, ypou can use this parameter to say at which value you start to encode tha auxillary boolean values needed by tseytin. By default, it's start at n+1 where n is the last integer used in the hash_bin dict
        
        Return :
            A pysat.formula.CNF object
        '''
        if hash_bin is None:
            hash_bin = self.bina
        if target is None:
            target = 0
        children = self.l_child
        clauses = []
        if method != "tseytin":
            m = 1
        else:
            m = -1

        if method != "comp":
            wantTarget = True
        else:
            wantTarget = False
        for c in children:
            clause = []
            if c[0] == "l" and (((np.argmax(c[1].left) != target) and not wantTarget) or (
                    (np.argmax(c[1].left) == target) and wantTarget)):
                id_lit = hash_bin[(c[1].num_feature, c[1].threshold)][0]
                clause.append(m * id_lit)
            elif c[0] == "r" and (((np.argmax(c[1].right) != target) and not wantTarget) or (
                    (np.argmax(c[1].right) == target) and wantTarget)):
                id_lit = hash_bin[(c[1].num_feature, c[1].threshold)][0]
                clause.append(-m * id_lit)
            if clause != []:
                current_node = c[1].parent
                while current_node is not None:
                    if current_node[0] == "l":
                        id_lit = hash_bin[(current_node[1].num_feature, current_node[1].threshold)][0]
                        clause.append(m * id_lit)
                    elif current_node[0] == "r":
                        id_lit = hash_bin[(current_node[1].num_feature, current_node[1].threshold)][0]
                        clause.append(-m * id_lit)
                    current_node = current_node[1].parent
                clauses.append(clause)
        n = len(hash_bin.keys())
        if method == "tseytin":
            if aux is None:
                clauses, n = enc.tseytin(clauses)
            else:
                clauses, n = enc.tseytin(clauses, aux)
        if threshold_clauses:
            clauses += self._threshold_clauses
        return CNF(from_clauses=clauses), n
        
    def to_DNF(self, target=None, hash_bin=None, method="comp", threshold_clauses=True, aux=None):
        '''
        Return a logical proposition DNF which is equivalent to the tree
        
        Parameters :
            target : int; say for which label the DNF is true
            hash_bin : dict; A dict corresponding to a hashmap (num_feature, threshold) <-> (associated boolean, number of appearence) NB : You can use a dict saying only the associated boolean
        
        Return :
            A pysat.formula.DNF object
        '''
        if hash_bin is None:
            hash_bin = self.bina
        if target is None:
            target = 0
        children = self.l_child
        clauses = []
        m = -1

        if method != "comp":
            wantTarget = True
        else:
            wantTarget = False
        for c in children:
            clause = []
            if c[0] == "l" and (((np.argmax(c[1].left) == target) and not wantTarget) or (
                    (np.argmax(c[1].left) == target) and wantTarget)):
                id_lit = hash_bin[(c[1].num_feature, c[1].threshold)][0]
                clause.append(m * id_lit)
            elif c[0] == "r" and (((np.argmax(c[1].right) == target) and not wantTarget) or (
                    (np.argmax(c[1].right) == target) and wantTarget)):
                id_lit = hash_bin[(c[1].num_feature, c[1].threshold)][0]
                clause.append(-m * id_lit)
            if clause != []:
                current_node = c[1].parent
                while current_node is not None:
                    if current_node[0] == "l":
                        id_lit = hash_bin[(current_node[1].num_feature, current_node[1].threshold)][0]
                        clause.append(m * id_lit)
                    elif current_node[0] == "r":
                        id_lit = hash_bin[(current_node[1].num_feature, current_node[1].threshold)][0]
                        clause.append(-m * id_lit)
                    current_node = current_node[1].parent
                clauses.append(clause)
        n = len(hash_bin.keys())
        
        if threshold_clauses:
            clauses += self._threshold_clauses
            
        return CNF(from_clauses=clauses), n
    
            

    def list_direct_reason(self, hash_bin=None):
        '''
        Return a logical proposition as CNf or a DNF which is equivalent to the tree
        
        Parameters :
            hash_bin : If you want tu use a different hashmap that the basic hash_map of the tree (In the case where the tree is in a random forest for example)
            
        Returns :
            A dict where the key is the different target available and the values a list of direct reason
            
        '''
        if hash_bin is None:
            hash_bin = self.bina
        l = [i for i in range(len(self.labels))]
        output = {}
        for k in l:
            output[k] = []
        for c in self.l_child:
            dr = []
            id_lit = hash_bin[(c[1].num_feature, c[1].threshold)][0]
            if c[0] == "l":
                classe = np.argmax(c[1].left)
                dr.append(-id_lit)
            elif c[0] == "r":
                classe = np.argmax(c[1].right)
                dr.append(id_lit)
            current_node = c[1].parent
            while current_node is not None:
                id_lit = hash_bin[(current_node[1].num_feature, current_node[1].threshold)][0]
                if current_node[0] == "l":
                    dr.append(-id_lit)
                elif current_node[0] == "r":
                    dr.append(id_lit)
                current_node = current_node[1].parent
            output[classe].append(dr)
        return output

    def erase_attribute(self, attribute):
        '''
        Create a tree that doesn't contain any node using the attribute 'attribute'' NB : It's a NON BOOLEAN attribute and it's an index to an ORIGINAL feature of the dataset treated
        Parameters :
            attribute: int; positive -> right child, negative -> left child

        Returns :
            a tree without the attribute
        '''
        self._root = self._root._erase_attribute(attribute)
        return self

    def is_valid(self, target=1):
        return self._root._is_valid(target)

    def is_sufficient_reason(self, implicant, target, hash_bin=None, delta=1):
        '''
        Say if an implicant is a sufficient reason to have the class taget
        
        Parameters:
            implicant : List of int; list which represents the implicant (in term of boolean attributes) . the absolute value is the number of the attribute and the sign say if it's true or false
            target : int; class we look for
            delta : float between 0 and 1 : delta-probable reason, if delta == 1 we look for a sufficient reason
            hash_bin : If you want tu use a different hashmap that the basic hash_map of the tree

        Returns:
            boolean which is true if implicant is a sufficient_reason
        '''
        if hash_bin is None:
            hash_bin = self.bina
        score = self._root._is_sufficient_reason(implicant, target, hash_bin)
        return score[1] * 100 >= int(delta * 100) * (score[0] + score[1])

    def binarized_instance(self, instance, pref_order=None, hash_bin=None):
        """
        Binarized an instance according to the binarization of the tree

        Parameters :
            instance: a list/numpy array representing the feature's values of an instance
            
        Returns:
            A list corresponding to the binarized instance
        """
        if hash_bin is None:
            hash_bin = self._bina
        output = []
        if pref_order is None:
            for k in hash_bin.keys():
                if instance[k[0] - 1] > k[1]:
                    output.append(hash_bin[k][0])
                else:
                    output.append(-hash_bin[k][0])
        else:
            for att in pref_order:
                for k in hash_bin.keys():
                    if k[0] - 1 == att:
                        if instance[att] > k[1]:
                            output.append(hash_bin[k][0])
                        else:
                            output.append(-hash_bin[k][0])
            output.reverse()  # I reverse the list here to begin to try to elimanate booleans linked to the less important attribute
        return output

    def unredundant_binarized_instance(self, instance_bin):
        """
        Binarized an instance according to the binarization of the tree

        Parameters :
            instance_bin: a list/numpy array representing the instance in his binary version
            
        Returns:
            A list corresponding to the binarized instance without redundant information i.e. feature a > 3 and feature_a > 2, we keep only the int linked too the boolean corresponding to feature_a > 3
        """
        pair_pos = {}
        pair_neg = {}
        for k in self._bina.keys():
            if self.bina[k][0] in instance_bin:
                pair_pos[k[0]] = k[1]
            if -self.bina[k][0] in instance_bin:
                pair_neg[k[0]] = k[1]
        output = []
        for k in pair_pos.keys():
            output.append(self.bina[(k, np.max(pair_pos[k]))][0])
        for k in pair_neg.keys():
            output.append(-self.bina[(k, np.min(pair_neg[k]))][0])
        return output

    def unbinarized_instance(self, instance_bin, need_detail=False):
        """
        Binarized an instance according to the binarization of the tree

        Parameters :
            instance_bin: a list/numpy array representing the instance in his binary version
            
        Returns:
            A list corresponding to the indices of the original attributes present in instance_bin   
        """
        output = []
        if not need_detail:
            for k in self._bina.keys():
                if (self.bina[k][0] in instance_bin) or (-self.bina[k][0] in instance_bin):
                    output.append(k[0])
            return list(set(output))
        else:
            instance_bin = self.unredundant_binarized_instance(instance_bin)
            for k in self._bina.keys():
                if (self.bina[k][0] in instance_bin):
                    output.append([k[0], k[1], "+"])
                elif (-self.bina[k][0] in instance_bin):
                    output.append([k[0], k[1], "-"])
            return output

    def find_sufficient_reason(self, instance, target=None, hash_bin=None, implicant=None, delta=1, pref_order=None):
        '''
        Find a sufficient reason of the feature using the tree structure

        Parameters :
            instance : numpy array or list; represent a instance by containing it's value for each attributes
            target : int, class targeted
            hash_bin : dict, binarization use
            implicant : list of int; represent an eventual knowed binarized implicant
            delta : float between 0 and 1 ; say delta in case of delta-probable reason. By default is 1 to look for sufficient reason
            pref_order : List of unique int from 0 to number of attributes non binarized - 1; Say for each original attribute, an order of preference which say at which point we want to keep the feature in our explanation. The first element of trhe list is the index of the mosyt important feature to try to keep in our explanation
            
        Returns :
            List containing a sufficient reason (Conjonction  of litterals)
        '''
        if hash_bin is None:
            hash_bin = self._bina
        if target is None:
            target = self.take_decision((instance))
        if implicant is None:
            implicant = self.binarized_instance(instance, pref_order=pref_order, hash_bin=hash_bin)
        i = 0
        while i < len(implicant):
            candidate = implicant.copy()
            candidate.pop(i)
            if self.is_sufficient_reason(candidate, target, hash_bin=hash_bin, delta=delta):
                implicant = candidate
            else:
                i += 1
        return implicant

    def find_direct_reason(self, instance, hash_bin=None):
        """
        Return the decision path used to classify the feature.

        Parameters :
            instance : numpy array or list representing a feature

        Returns :
            A list containing the path encoding
        """
        if hash_bin is None:
            hash_bin = self._bina
        return self.root._decision_path(instance, hash_bin)

    def find_min_reason(self, instance, target=None, hash_bin=None, implicant=None, *, nb=1):
        """
        Find a minimal reason of the feature using the tree structure

        Parameters :
            instance : numpy array or list; represent a instance by containing it's value for each attributes
            target : int, class targeted
            hash_bin : dict, binarization use
            implicant : list of int; represent an eventual knowed binarized implicant
    
        Returns :
            List containing a minimal reason (Conjonction  of litterals)
        """
        if hash_bin is None:
            hash_bin = self.bina
        if target is None:
            target = self.take_decision((instance))
        if implicant is None:
            implicant = self.binarized_instance(instance)
        CNF_arbre = self.to_CNF(hash_bin=hash_bin, target=target, threshold_clauses=False)[0].clauses
        # Generate our clauses
        CNF_min = WCNF()

        for l in implicant:  # soft
            CNF_min.append([-l], weight=1)

        for clause in CNF_arbre:  # hard
            new_clause = []
            for l in clause:
                if l in implicant:
                    new_clause.append(l)
            assert new_clause != []
            CNF_min.append(new_clause)
        first = True
        results = []
        for i in range(nb):
            with RC2(CNF_min) as rc2:
                result = rc2.compute()
            output = []
            if result == None:
                return results
            for l in result:
                if l in implicant:
                    output.append(l)
            assert (self.is_sufficient_reason(output, target))
            if nb == 1:
                return output
            if first:
                CNF_min.extend(PBEnc.atmost(lits=implicant, top_id=CNF_min.nv + 1, bound=len(output)).clauses)
            CNF_min.append([-l for l in output])
            first = False
            results.append(output)
        return results

    def compileTree(self, hash_bin=None, target=None):
        """
        Creat a list of int describing a tree
        
        Parameters:
            implicant : List of int; list which represents the implicant. the absolute value is the number of the attribute and the sign say if it's true or false
            target : int; class we look for
        
        Returns :
            list of int
        """
        if hash_bin is None:
            hash_bin = self.bina
        if target is None:
            target = 0
        out = self.root._compileTree(0, hash_bin=hash_bin, target=target)
        out[0].append(out[1])
        return out[0]

    def extract_core_cnf(self, instance, target=None, hash_bin=None, implicant=None):
        if hash_bin is None:
            hash_bin = self.bina
        if target is None:
            target = self.take_decision((instance))
        if implicant is None:
            implicant = self.binarized_instance(instance)
        CNF_arbre = self.to_CNF(hash_bin=hash_bin, target=target, threshold_clauses=False)[0].clauses
        # Generate our clauses
        newCNF = []
        for clause in CNF_arbre:  # hard
            new_clause = [l for l in clause if l in implicant]
            newCNF.append(new_clause)
            assert new_clause != []

        newCNF = sorted(newCNF, key=lambda c: len(c))
        flags = [0 for i in range(len(implicant) + 1)]
        subsumed = [0 for i in range(len(newCNF) + 1)]
        for i in range(len(newCNF)):
            if subsumed[i] == 1:
                continue
            for l in newCNF[i]:
                flags[abs(l)] = 1
            for j in range(i + 1, len(newCNF)):
                tmp = 0
                for l in newCNF[j]:
                    if flags[abs(l)] == 1:
                        tmp = tmp + 1
                if tmp == len(newCNF[i]):
                    subsumed[j] = 1
            for l in newCNF[i]:
                flags[abs(l)] = 0
        return [cl for i, cl in enumerate(newCNF) if subsumed[i] == 0]

    def find_necessary_features(self, instance, target=None, hash_bin=None, implicant=None):
        """
        Find necessary/relevant features using the tree structure

        Parameters :
            instance : numpy array or list; represent a instance by containing it's value for each attributes
            target : int, class targeted
            hash_bin : dict, binarization use
            implicant : list of int; represent an eventual knowed binarized implicant

        Returns :
            tuple containing   (necessary, relevant)
        """
        newCNF = self.extract_core_cnf(instance)

        necessary = {c[0] for c in newCNF if len(c) == 1}
        relevant = {l for i, cnf in enumerate(newCNF) if len(cnf) > 1 for l in cnf}
        return (necessary, relevant)

    def generate_CNF_PI(self, instance):
        """
        generate formula used to enumerate all PI or to create heatmap of features
        Based on Saïd Jabbour, João Marques-Silva, Lakhdar Sais, Yakoub Salhi:
              Enumerating Prime Implicants of Propositional Formulae in Conjunctive Normal Form. JELIA 2014: 152-165
        No necessary to add extra literals, formula is already monotone
        """

        cnf = self.extract_core_cnf(instance)
        necessary = {c[0] for c in cnf if len(c) == 1}
        size = int(max(abs(l) for c in cnf for l in c))
        instance2solver = [0 for i in range(size + 1)]
        solver2instance = [0]  # useless
        nb_lits = 1
        # create mapping between formula in glucose and instance
        for cl in cnf:
            if len(cl) == 1:
                continue
            for l in cl:
                if instance2solver[abs(l)] != 0:
                    continue
                instance2solver[abs(l)] = nb_lits
                solver2instance.append(l)
                nb_lits = nb_lits + 1

        # work with lit from 1 to ..
        newcnf = []
        for cl in cnf:
            if (len(cl) == 1):
                continue
            newcnf.append([instance2solver[abs(l)] for l in cl])

        # create occurrences
        occurrences = [[] for i in range(nb_lits)]
        for i, cl in enumerate(newcnf):
            for l in cl:
                occurrences[l].append(i)

        # add bijection (see Jelia paper)
        bijection = []
        add_lits = nb_lits
        for l in range(1, nb_lits):
            clause = [-l]
            for j in occurrences[l]:
                cl = newcnf[j]
                if len(cl) == 2:
                    clause.append(-cl[0] if cl[1] == l else -cl[1])
                    continue
                clause.append(add_lits)
                # nblit = -l1 and -l2 ... Add to bijection (tseitsin
                tmp_clause = [add_lits]
                for l2 in cl:
                    if l2 == l:
                        continue
                    bijection.append([-add_lits, -l2])
                    tmp_clause.append(l2)
                bijection.append(tmp_clause)
                add_lits = add_lits + 1
            bijection.append(clause)

        return (solver2instance, instance2solver, necessary, nb_lits, add_lits, newcnf + bijection)

    def enumerate_all_sufficient(self, instance, *, max=-1):
        """
        enumerate all syfficient reasons (prime implicants.
        """
        glucose2instance, instance2glucose, necessary, nb_lits, total_lits, clauses = self.generate_CNF_PI(instance)
        # add formula to glucose
        glucose = Glucose4()
        target = self.take_decision(instance)

        for cl in clauses:
            glucose.add_clause(cl)

        sufficients = []
        while True:
            result = glucose.solve()
            if result == False or (max != -1 and len(sufficients) >= max):
                break
            model = glucose.get_model()
            sufficient = [l for l in necessary] + [glucose2instance[l] for l in model if l > 0 and abs(l) < nb_lits]
            assert (self.is_sufficient_reason(sufficient, target))
            sufficients.append(sorted(sufficient, key=lambda l: abs(l)))
            # block this implicant
            glucose.add_clause([-l for l in model if l > 0 and abs(l) < nb_lits])

        return sufficients

    def heatmap_contrastive(self, instance):
        contrastive = self.enumarate_all_contrastive(instance)
        heat = {}
        for clause in contrastive:
            for l in clause:
                heat[l] = heat.get(l, 0) + (1 / len(clause))

        return heat

    def heatmap_sufficients(self, instance, *, time_out=None):
        """
        create the heatmap: the number of PI where features occurs
        """
        glucose2instance, instance2glucose, necessary, nb_lits, total_lits, clauses = self.generate_CNF_PI(instance)

        # special case when necessary are alone in sufficient....
        if len(clauses) == 0:
            heat = {}
            for n in necessary:
                heat[n] = 1
            return heat

        # create CNF
        total_lits -= 1
        hash = str(uuid.uuid4().fields[-1])[:8]
        file = open(f"/tmp/heat-{hash}.cnf", "w")
        file.write(f"p cnf {total_lits} {len(clauses)}\n")
        for c in clauses:
            line = ''
            for l in c:
                line += str(l) + ' '
            file.write(line + '0\n')
        file.close()

        # create query
        query = open(f"/tmp/heat-{hash}.query", "w")
        query.write(f"p cnf {total_lits} {len(clauses)}\n")
        query.write("m 0\n")
        for l in range(1, nb_lits):
            query.write("m" + str(l) + ' 0\n')
        query.close()

        # call d4
        try:
            p = subprocess.run(["/home/audemard/expectation/softwares/dtandrf_intel_python/bin/d4_static", "-m", "ddnnf-compiler", "-i",
                                f"/tmp/heat-{hash}.cnf", "--query", f"/tmp/heat-{hash}.query"], timeout=time_out,
                               capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            return {1: -1}
        output_str = p.stdout
        nb_models = [int(line.split(" ")[1]) for line in output_str.split("\n") if len(line) > 0 and line[0] == "s"]
        nb_necessary = nb_models[0] if len(nb_models) > 0 else 1
        heat = {}
        for n in necessary:
            heat[n] = nb_necessary
        for l in range(1, nb_lits):
            heat[glucose2instance[l]] = nb_models[l]
        return heat

    def enumarate_all_contrastive(self, instance):
        newCNF = self.extract_core_cnf(instance)
        return newCNF

    def reason_with_max_of_type(self, instance, type):

        target = self.take_decision((instance))
        implicant = self.binarized_instance(instance)
        hash_bin = self.bina
        CNF_arbre = self.to_CNF(hash_bin=hash_bin, target=target, threshold_clauses=False)[0].clauses

        # Generate our clauses
        CNF_min = WCNF()

        for clause in CNF_arbre:  # hard
            new_clause = []
            for l in clause:
                if l in implicant:
                    new_clause.append(l)
            CNF_min.append(new_clause)

        top_weight = len(implicant) + 1
        for l in implicant:  # soft
            if l * type > 0:
                CNF_min.append([-l], weight=top_weight)
            else:
                CNF_min.append([-l], weight=1)

        with RC2(CNF_min) as rc2:
            result = rc2.compute()
        return [l for l in result if l in implicant]

    def reason_with_min_positive(self, instance):
        return self.reason_with_max_of_type(instance, 1)

    def reason_with_min_negative(self, instance):
        return self.reason_with_max_of_type(instance, -1)


    def convert_binary_cnf_to_feature_names(self, cnf, features_name):
        """
        Converts a binary representation of a CNF into a human-readable format 
        using the original feature names from the dataset.

        Args:
            cnf: The CNF formula represented using binary variables (integers).

            features_name: List of feature names from the original dataset corresponding 
                                    to the decision tree structure.

        Returns:
            list[list[str]]: A CNF formula where each condition is expressed using the corresponding 
                            feature name and threshold in readable format (e.g., "Age < 45.0").
        """
        bina_tree = {v[0]: k for k,v in self.bina.items()}

        cnf_to_numeric = [
            [
                f"{features_name[bina_tree[abs(x)][0] - 1]}  >  {bina_tree[abs(x)][1]}"
                if x >= 0
                else f"{features_name[bina_tree[abs(x)][0] - 1]}  <  {bina_tree[abs(x)][1]}"
                for x in clause
            ]
            for clause in cnf
        ]

        return cnf_to_numeric
    
    def convert_binary_term_to_feature_names(self, term, features_name):
        """
        Converts a binary term (i.e., a list of signed literals) into a human-readable representation using the original feature names.
        Args:
            term (List[int]): A binary term representing a conjunction of conditions,

            features_name (List[str]): A list of original dataset feature names, indexed by column order.

        Returns:
            List[str]: A list of strings representing the term in readable feature-threshold format, 
            e.g., ["Age > 45.0", "BMI < 25.0"]
        """
        bina_tree = {v[0]: k for k,v in self.bina.items()}

        term_to_numeric = [
                f"{features_name[bina_tree[abs(x)][0] - 1]}  >  {bina_tree[abs(x)][1]}"
                if x >= 0
                else f"{features_name[bina_tree[abs(x)][0] - 1]}  <  {bina_tree[abs(x)][1]}"
                for x in term
            ]

        return term_to_numeric
    
    def restrict_cnf_to_instance(self, cnf, implicant):
        """
        Restricts a CNF formula to a given binary instance by keeping only the literals that are present in the instance's implicant.

        Args:
        cnf (List[List[int]]): A list of clauses representing a CNF formula, where each clause is a list of integer literals.

        implicant (List[int]): A list of literals (integers) representing the binary 
            encoding of an instance that satisfies a particular decision path in the model.

        Returns:
            List[List[int]]: The restricted CNF, with each clause containing only the literals that appear in the instance's implicant.
        """
        restrict_cnf = [
            [literal for literal in clause if literal in implicant]
            for clause in cnf
        ]
        return restrict_cnf



class decision_node:
    '''
    A decision_tree is made of decision_node
    '''

    def __init__(self, nb_features, num_feature, threshold, probabilities, parent=None, left=None, right=None):
        '''
        Allow to construct a decision node
        
        Parameters :
            nb_feature : int; represents the number of element in a vector that we need to classify
            num_feature : int; give the indices of the feature studied by this node to take its decision
            threshold : float; if the feature studied is less or equal to the threshold, we will continue our way with the child on the left
            probabilities : numpy array; Contains the probabilities to conclude for each class at this node
            parent : a couple (string, decision_node) : string = 'r' or 'l' for 'right' or 'left' saying if this node is the left or right child of decision_node
            left : decision_node : a left child
            right : decision_node : a right child
            
        Returns : 
            a decision_node
            
        '''
        if (num_feature >= 0) and (nb_features >= 0) and (np.sum(np.array(probabilities) >= 0) == len(probabilities)):
            self.nb_features = nb_features
            if num_feature <= nb_features:
                self.num_feature = num_feature
                self.threshold = threshold
                self.probabilities = probabilities
                self._left = left
                self._right = right
                self._parent = parent
            else:
                raise AssertionError("Couldn't have num_feature >= nb_features")
        else:
            raise ValueError(
                f"num_feature : {num_feature}, nb_feature : {nb_features} or something in probabilities : {probabilities} is negative")

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        if type(left) == decision_node and len(self.probabilities) == len(
                left.probabilities) and self.nb_features == left.nb_features:
            left.parent = ("l", self)
            self._left = left
        elif (np.sum(left >= 0)) == len(left):
            self._left = left
        else:
            raise ValueError(
                "nb_features and len(probabilities) have to be the same between the parent node and his child, or left can be an array of probabilities")

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if type(parent[1]) == decision_node and len(self.probabilities) == len(
                parent[1].probabilities) and self.nb_features == parent[1].nb_features:
            self._parent = parent
        else:
            raise ValueError(
                "nb_features and len(probabilities) have to be the same between the parent node and his child")

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        if type(right) == decision_node and len(self._probabilities) == len(
                right.probabilities) and self.nb_features == right.nb_features:
            right.parent = ("r", self)
            self._right = right
        elif ((np.sum(right >= 0)) == len(right)):
            self._right = right
        else:
            raise ValueError(
                "nb_features and len(probabilities) have to be the same between the parent node and his child")

    @property
    def num_feature(self):
        return self._num_feature

    @num_feature.setter
    def num_feature(self, num_feature):
        if (num_feature <= self.nb_features and num_feature >= 0):
            self._num_feature = num_feature
        else:
            raise ValueError("num_feature must be positive and inferior than nb_features")

    @property
    def probabilities(self):
        return self._probabilities

    @probabilities.setter
    def probabilities(self, probabilities):
        ok = True
        for i in probabilities:
            if i < 0:
                ok = False
        if ok:
            self._probabilities = probabilities
        else:
            raise ValueError("All probabilities must be positive")

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        self._threshold = threshold

    def take_decision(self, instance):
        '''
        Give the classification of a feature according to this node
        
        Parameters :
            instance : numpy array of float; vector corresponding to the values of the studied feature
    
        Returns : 
            int; a integer corresponding to the decided class
        '''
        elmt = instance[self.num_feature - 1]
        if elmt <= self.threshold:  # if the element of our feature is less ou equal to the node threshold we decide to consult our left child
            if type(self.left) == decision_node:
                return self.left.take_decision(instance)  # If there isn't any left child, then we take a decision now
            else:
                return np.argmax(self.left)
        else:  # if not; we continue our way with the right child
            if type(self.right) == decision_node:
                return self.right.take_decision(instance)  # If there isn't any right child, then we take a decision now
            else:
                return np.argmax(self.right)

    def _erase_attribute(self, attribute):
        '''
        Create a tree that doesn't contains the attribute'
        
        Parameters :
            feature : numpy array or list; represent a binarized feature

        Returns :
            a my_node
        '''
        if self._num_feature == attribute:
            return self.right
        elif self.num_feature == -attribute:
            return self.left
        else:
            if type(self._left) == decision_node:
                self._left = self._left._erase_attribute(attribute)
            if type(self._right) == decision_node:
                self._right = self._right._erase_attribute(attribute)
            return self

    def _is_valid(self, target):
        ''' 
        Say if a tree is valid according to its targeted value
        
        Parameters:
            target : int; class we look for
            
        Returns:
            boolean
        '''
        if type(self._left) != decision_node:
            output = target == np.argmax(self._left)
        else:
            output = self._left._is_valid(target)
        if type(self._right) != decision_node:
            output = output and (target == np.argmax(self._right))
        else:
            output = output and self._right._is_valid(target)
        return output

    def _is_sufficient_reason(self, implicant, target, hash_bin, var_fixed=[]):
        '''
        Say if an implcant is a sufficient reason to have the class taget
        
        Parameters:
            implicant : List of int; list which represents the implicant. the absolute value is the number of the attribute and the sign say if it's true or false
            target : int; class we look for
            hash_bin : dict; a dictionnary which represents hos the tree was binarized
            var_fixed : list; internal parameter for recursion (contains literal already take into account)

        Returns:
            boolean
        '''
        # The attribute is in the implicant
        score = [0, 0]
        num_feature = hash_bin[(self.num_feature, self.threshold)][0]
        exposant = len(hash_bin) - len(implicant) - len(var_fixed)
        if num_feature in implicant:
            if type(self._right) != decision_node:
                if (target == np.argmax(self._right)):
                    score[1] += 1 * (2 ** exposant)
                else:
                    score[0] += 1 * (2 ** exposant)
                return score
            else:
                return self._right._is_sufficient_reason(implicant, target, hash_bin, var_fixed=var_fixed.copy())
        # The negation of the attribute is in the implicant
        elif -num_feature in implicant:
            if type(self._left) != decision_node:
                if (target == np.argmax(self._left)):
                    score[1] += 1 * (2 ** exposant)
                else:
                    score[0] += 1 * (2 ** exposant)
                return score
            else:
                return self._left._is_sufficient_reason(implicant, target, hash_bin, var_fixed=var_fixed.copy())
        # The attribute isn't in the implicant
        else:
            if (num_feature not in var_fixed) and (-num_feature not in var_fixed):
                var_fixed.append(num_feature)
                exposant -= 1
            if (type(self._left) != decision_node):
                if (target == np.argmax(self._left)):
                    score[1] += 2 ** (exposant)
                else:
                    score[0] += 2 ** (exposant)
            else:
                new = self._left._is_sufficient_reason(implicant, target, hash_bin, var_fixed=var_fixed.copy())
                score[1] += new[1]
                score[0] += new[0]
            if type(self._right) != decision_node:
                if (target == np.argmax(self._right)):
                    score[1] += 2 ** (exposant)
                else:
                    score[0] += 2 ** (exposant)
            else:
                new = self._right._is_sufficient_reason(implicant, target, hash_bin, var_fixed=var_fixed.copy())
                score[1] += new[1]
                score[0] += new[0]
            return score

    def node_to_text(self, depth=0):
        '''
        Return a String describing the node structure
        
        Parameter :
            depth : int; internal parameter (to know the current depth treated)
            
        Return :
            String describing the architecture from this node
        '''
        longueur = 11
        sortie = f'Feature {self.num_feature} > {self.threshold} --> '
        if type(self.right) == decision_node:
            sortie = sortie + self.right.node_to_text(depth + 1)
        else:
            sortie = sortie + f'classification : {np.argmax(self.right)}\n'
            for t in range(depth):
                sortie = sortie + longueur * ' ' + '|' + longueur * ' '
        if type(self.left) == decision_node:
            sortie = sortie + self.left.node_to_text(depth)
        else:
            sortie = sortie + f'classification : {np.argmax(self.left)}\n'
            for t in range(depth - 1):
                sortie = sortie + longueur * ' ' + '|' + longueur * ' '
        return sortie

    def searchChild(self):
        '''
        Return a list of tuple defining the child from this node
        '''
        output = []
        if type(self._left) != decision_node:
            output.append(('l', self))
        else:
            output += self._left.searchChild()
        if type(self._right) != decision_node:
            output.append(('r', self))
        else:
            output += self._right.searchChild()
        return output

    def hash_bin(self, last_lit=0):
        """
        Return a dictionnary corresponding to a binarisation of trhe dataset managed by the decision_tree from thos node
        
        Parameter :
            last_lit : int ; (internal parameter) say at which int we can start to encode
            
        Return :
            A dict (num_feature, threshold) -> (integer representing the boolean index, number of appereance)
        """
        output = {}
        output[(self.num_feature, self.threshold)] = [last_lit + 1, 1]

        if type(self._left) == decision_node:
            out_c = self._left.hash_bin(last_lit + 1)
            new_last = max([out_c[k] for k in out_c.keys()])[0]
            for k in out_c.keys():
                if output.get(k, None) is None:
                    output[k] = out_c[k]
                else:
                    output[k][1] += 1
        else:
            new_last = last_lit + 1

        if type(self._right) == decision_node:
            out_c = self._right.hash_bin(new_last)
            new_last = max([out_c[k] for k in out_c.keys()])
            for k in out_c.keys():
                if output.get(k, None) is None:
                    output[k] = out_c[k]
                else:
                    output[k][1] += 1

        return output

    def _decision_path(self, instance, hash_bin):
        """
        Return the decision path used to classify the feature.

        Parameters :
            instance : numpy array or list representing a feature
            hash_bin : dict; a dictionnary representing the binary encoding of the tree

        Returns :
            A list containing the path encoding
        """
        output = []
        elmt = instance[self.num_feature - 1]
        if elmt <= self.threshold:  # if the element of our feature is less ou equal to the node threshold we decide to consult our left child
            output.append(-hash_bin[(self.num_feature, self.threshold)][0])
            if type(self.left) == decision_node:
                return output + self.left._decision_path(instance,
                                                         hash_bin)  # If there isn't any left child, then we take a decision now
            else:
                return output
        else:  # if not; we continue our way with the right child
            output.append(hash_bin[(self.num_feature, self.threshold)][0])
            if type(self.right) == decision_node:
                return output + self.right._decision_path(instance,
                                                          hash_bin)  # If there isn't any right child, then we take a decision now
            else:
                return output

    def generate_instance(self, reason, hash_bin=None):
        """
        WARNING : Work ONLY with mnist dataset or a declinaison of it
        
        Create an instance matching with a known reason
        
        Parameters :
            reason : a list of int descvribing a reason ex : [-6,9,23,-25,42]
        
        Returns :
            A list corresponding to an instance that this forest can manage
        """
        if hash_bin is None:
            hash_bin = self._bina
        reverse_hash_bin = {}
        for k in hash_bin.keys():
            reverse_hash_bin[hash_bin[k][0]] = k
        instance = [int(np.random.rand(1)[0] * 255) for i in range(self.nb_features)]
        exp = self.unbinarized_instance(reason, need_detail=True)
        for e in exp:
            if e[2] == "+":
                instance[e[0] - 1] = e[1] + 1
            else:
                instance[e[0] - 1] = e[1] - 1
        return instance

    def _compileTree(self, nb_node, hash_bin, target):
        nb_node += 1
        output = [hash_bin[(self.num_feature, self.threshold)][0]]
        if type(self.left) == decision_node:
            out = self.left._compileTree(nb_node, hash_bin, target)
            output += out[0]
            nb_node = out[1]
        elif np.argmax(self.left) == target:
            output += [-1]
        else:
            output += [-2]
        if type(self.right) == decision_node:
            out = self.right._compileTree(nb_node, hash_bin, target)
            output += out[0]
            nb_node = out[1]
        elif np.argmax(self.right) == target:
            output += [-1]
        else:
            output += [-2]
        return output, nb_node
