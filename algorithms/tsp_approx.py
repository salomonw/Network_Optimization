# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:33:21 2018

@author: Salomon Wollenstein

Assymetric-TSO with log(n) guarantee
"""


def read_tsp_distances(input_file):
    # read the text file and create two vectors
    u = []
    with open(input_file) as f:
        cnt = 0 
        for line in f: 
            a = line.split()

            x = (map(float, a))
            u.append(map(int,x))
        return u

## min-weight disjoint cycle
def min_weight_disjoint_cycle(tsp_dist):
    # create a new model 
    m = Model('min-weight disjoint cover')
    
    # create variables
    n = len(tsp_dist)
    x = {}
    for i in range(n):
        for j in range(n):
            x[i,j] = m.addVar(vtype=GRB.BINARY, name='x_' + str(i) + '_' + str(j))
    
    # Add objective
    m.setObjective(quicksum(c[i][j] * x[i,j] for i in range(n) for j in range(n)), GRB.MINIMIZE)
    
    # Add constraints:
    m.addConstrs((quicksum(x[i,j] for i in range(n)) == 1 for j in range(n)) , "c1")
    m.addConstrs((quicksum(x[i,j] for j in range(n)) == 1 for i in range(n)) , "c2")
    
    m.optimize()
    
    x1 = []
    for v in m.getVars():
        x1.append(v.x)
        #print(v.varName, v.x)
    
    #print('Obj:', m.objVal)
    
    x1 = {}
    for i in x.keys():
        x1[i] = x[i].x
    
    return x1, m.objVal
    

def nodes_to_distMat(nodes, tsp_dist):
    dist_new = []
    cnt = 0
    for i in nodes:
        dist_new.append(i)
        dist_new[cnt] = []
        for j in nodes:
            dist_new[cnt].append(tsp_dist[i][j])
            
        cnt = cnt + 1
    return dist_new


def create_graph(x1):
    H = nx.Graph()
    for k, v in x1.keys():
        if x1[(k,v)] > 0 :
            H.add_edge(k, v)
    return H


def relabel_graph(x1, G_nodes):
    x2 = {}
    for x in x1.keys():
        key = (G_nodes[x[0]], G_nodes[x[1]])
        x2[key] = x1[x]
    return x2
    
def plot_graph(H):
    pos=nx.kamada_kawai_layout(H)
    plt.figure()
    labels=nx.draw_networkx_labels(H,pos)
    for i in H.nodes():
        labels[i] = i
        
    nx.draw_networkx_nodes(H,pos,
                           nodelist=list(H.nodes()),
                           node_color='r',
                           node_size=200,
                           alpha=0.8)
    
    nx.draw_networkx_edges(H,pos,
                           edgelist=list(H.edges()),
                           width=4,alpha=0.5,edge_color='r')
    
    nx.draw_networkx_labels(H,pos,labels,font_size=12)
    #nx.draw_networkx_edges(H,pos,width=1.0,alpha=0.5)
    
    
import os 
import numpy as np
from gurobipy import *

import networkx as nx
import matplotlib.pyplot as plt
import random

# Reading files
os.chdir('G:/My Drive/Github/Network_Optimization/algorithms')
input_file = '../tsp_data/atsp.txt'
tsp_dist = read_tsp_distances(input_file)
c = tsp_dist 
cost = []

# solve first problem
x1, obj = min_weight_disjoint_cycle(tsp_dist)
cost.append(obj)
H1 = create_graph(x1)

plot_graph(H1)

# get different cycles
disj_G = list(nx.connected_component_subgraphs(H1))


G0 = H1

while len(disj_G)> 1 :
    G_nodes = []
    for G in disj_G:
        # choose a random node
        i = random.choice(list(G.nodes()))
        # list of nodes
        G_nodes.append(i)
    
    dist_mat = nodes_to_distMat(G_nodes, tsp_dist)
    x1, obj = min_weight_disjoint_cycle(dist_mat)
    cost.append(obj)
    x1 = relabel_graph(x1, G_nodes)
    H = create_graph(x1)
    G0 = nx.compose(G0,H)
    
    disj_G = list(nx.connected_component_subgraphs(H))
    plot_graph(G0)


total_cost = np.sum(cost)

print('the total cost is: '+ str(total_cost))