# **Packages**



# Python package
import sys
sys.path.append('build')
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, LeaveOneGroupOut
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from math import *

# Pysat packages
from pysat.card import *
from pysat.pb import PBEnc
from pysat.formula import WCNF, CNF
from pysat.pb import *
from pysat.examples.rc2 import RC2
from pysat.solvers import Glucose4
from pysat.solvers import Solver, Minisat22

#ours package 
import my_tree as mt
import my_tree

# SAT encoding of "Arenas et al 2022" packages
import utils
import dtree
import gen_dt
import encoder 

# import help function and error function 
from UAI_Functions import W_f, M_s, D_s, Approx_ascendant, Approx_descent, Dichotomie


# **Learn DT and import the dataset**

data = pd.read_csv('tic-tac-toe.csv')
df = data.copy()
ind = df.columns[-1]
y = df[ind]
X = df.drop(ind, axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

my_tree = mt.decision_tree()
my_tree.from_DecisionTreeClassifier(dt)


# **Example of application of our algorithms and binary search with tic_tac_toe**

i = 0# the index of instance
file = 'data_dt'# if you want to change the name, you need to change it also in Dichotomie function
dim = data.shape[1]
ind = X_test.index[i]
pred = dt.predict(X_test)[i]
ins = list(X_test.loc[ind]) + [pred]
instance = X_test.loc[ind]
target = my_tree.take_decision(instance=instance)
dnf = my_tree.to_DNF(target=target, threshold_clauses=False)[0].clauses
phi = my_tree.to_DNF(target=1-target, threshold_clauses=False)[0].clauses
implicant = my_tree.binarized_instance(instance=instance)
n = len(my_tree.bina)
R_d = my_tree.find_direct_reason(instance=instance) # direct reason 
R = my_tree.unbinarized_instance(R_d)
gen_dt.dt_to_file(dimension = dim, dt=dt, filename=file, desired_n_leaves=80, positive_class=pred) 


print('the size of direct reason is: {}'.format(len(R_d))) 


GD = Approx_descent(phi=phi, I_s=R_d, n=n, k=4)
GA = Approx_ascendant(phi=phi, I_s=R_d, n=n, k=4)

print("the output of GD is: {} and GA is: {}".format(GD, GA))


# **To get the error of GA and GD**


print("error of GD is: {} and the error of GA is: {}".format(W_f(phi, GA, n), W_f(phi, GD, n)))


"""
For more information about SAT encoding, see https://arxiv.org/abs/2207.12213
"""
di = Dichotomie(a=0, b=1, k=4, ins=ins, R=R, e=0.001)
print("the error of binary search is: {}".format(1-di))


data = pd.read_csv('mnist49.csv')
df = data.copy()
ind = df.columns[-1]
y = df[ind]
X = df.drop(ind, axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

my_tree = mt.decision_tree()
my_tree.from_DecisionTreeClassifier(dt)


i = 2 # the index of instance
file = 'data_dt'
dim = data.shape[1]
ind = X_test.index[i]
pred = dt.predict(X_test)[i]
ins = list(X_test.loc[ind]) + [pred]
instance = X_test.loc[ind]
target = my_tree.take_decision(instance=instance)
dnf = my_tree.to_DNF(target=target, threshold_clauses=False)[0].clauses
phi = my_tree.to_DNF(target=1-target, threshold_clauses=False)[0].clauses
implicant = my_tree.binarized_instance(instance=instance)
n = len(my_tree.bina)
R_d = my_tree.find_direct_reason(instance=instance) # direct reason 
R = my_tree.unbinarized_instance(R_d)
gen_dt.dt_to_file(dimension = dim, dt=dt, filename=file, desired_n_leaves=80, positive_class=pred) 



print('the size of direct reason is: {}'.format(len(R_d))) 


GD = Approx_descent(phi=phi, I_s=R_d, n=n, k=7)
GA = Approx_ascendant(phi=phi, I_s=R_d, n=n, k=7)

print("the output of GD is: {} and GA is: {}".format(GD, GA))


print("error of GD is: {} and the error of GA is: {}".format(W_f(phi, GA, n), W_f(phi, GD, n)))


# **Now, if you want to check a binary search**

di = Dichotomie(a=0, b=1, k=3, ins=ins, R=R, e=0.001)
print("the error of binary search is: {}".format(1-di))


print("Sorry, that is not possible")

