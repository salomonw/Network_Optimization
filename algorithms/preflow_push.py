# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:32:31 2018

@author: Salomon
"""


execfile('linked_list.py')
execfile('find_path.py')

# Augmenting path 
input_file = 'medflow.txt'

source_node = 1
target_node = 300

nextOut, nextIn, x, U, fOut, fIn, arcs = read_linked_list(input_file)
arcs_dict = {str(v): k for k, v in arcs.items()}


max_flow = 0

# Preprocess
def preprocess(source_node, target_node, nextOut, nextIn, U, fOut, fIn, arcs, arcs_dict):
    x = {}
    e = {}
    
    numNodes = len(fIn)
    numEdges = len(U)
    
    for k in arcs:
        x[(arcs[k][0], arcs[k][1]) ] = 0 
    
    pred, d = dijkstra_linked_list(source_node, target_node, nextOut, nextIn, U, fOut, fIn, arcs, x)
    
    for k in range(numNodes):
        d[k+1] = d[target_node] - d[k+1]
        e[k+1] = 0
        
    k = fOut[source_node] # node adjacent to source
    j = arcs[k][1] # edge connecting nodes
    x[(source_node, j)] = U[k] # push as much as capacity
    d[source_node] = numNodes
    e[j] = U[k]
    U[k] = 0
    
    k = nextOut[k] 
    while k > 0:
        j = arcs[k][1]
        x[(source_node, j)] = U[k] # push as much as capacity  
        e[j] = U[k]    
        U[k] = 0
        k = nextOut[k] # node adjacent to source
 
        
    return x, d, e, U


def push_relabel(i, e, x, d, U):
    
    delta = 0
    k = fOut[i]
    if k > 0 :
        j = arcs[k][1]
    while k > 0:    
        if d[i] >= d[j] + 1 and U[k] > 0:      
            delta = min(e[i], U[k])
            x[(i, j)] = x[(i, j)] + delta
            e[i] = e[i] - delta
            e[j] = e[j] + delta
            U[k] = U[k] - delta
            return x, e, d, U
        k = nextOut[k]
        if k > 0:
            j = arcs[k][1]
        
            
    k2 = fIn[i]
    if k2 > 0 :
       # i = arcs[k2][1]
        j = arcs[k2][0]
    while k2 > 0:
        if d[i] >= d[j] + 1 and x[(j, i)] > 0:
            delta = min(e[i], x[(j, i)])
            x[(j, i)] = x[(j, i)] - delta
            e[i] = e[i] - delta
            e[j] = e[j] + delta
            U[k2] = U[k2] + delta
            #print(' ----------------------')
            #pause()
            return x, e, d, U
        k2 = nextIn[k2] 
        if k2 > 0 :
            j = arcs[k2][0]
   
    #print(k2)
   # print('------')
    A = []
    B = [1000]
    k = fOut[i]
    k2 = fIn[i]
    while k > 0:
       # pause()
        #print(' ----------------------')
        if U[k] > 0:
            j = arcs[k][1]
            A.append(j)
         #   print(' ----------------------')
            #B.append(U[k])
        k = nextOut[k] 
            
    while k2 > 0:
        #pause()
        j = arcs[k2][0]
        if x[(j, i)] > 0 :
            #j = arcs[k2][1]
      #      print(' ----------------------')
            A.append(j)
            #B.append(U[k2])
            #A.append(U[k2])
        k2 = nextIn[k2]
    
    if len(A) > 0:
        #d[i] = min(min([d[j]+1 for j in A]), min(B))
        d[i] = min([d[j]+1 for j in A])
    return x, e, d, U
                


## Dijkstra's
def dijkstra_linked_list(source_node, target_node, nextOut, nextIn, U, fOut, fIn, arcs, flow):
    numNodes = len(fIn)
    numEdges = len(U)
      
    Q = []
    pred = {}
    d ={}
    
    for k in range(numNodes):
        d[k+1] = 9999999999
    
    d[source_node] = 0
    
    Q.append(source_node)
    
    while len(Q) > 0:
        i = Q[0]
        
        if fOut[i] > 0:
            e = fOut[i]
            j = arcs[e][1]
            
            if d[i] + 1 <= d[j] and U[e]>0:
                d[j] = d[i] + 1
                pred[j] = i
                Q.append(j)
            
            while nextOut[e] > 0:
                e = nextOut[e]
                j = arcs[e][1]
                
                if d[i] + 1 <= d[j] and U[e]>0:
                    d[j] = d[i] + 1   
                    pred[j] = i
                    Q.append(j)
                    
        elif fIn[i] > 0:
            e = fIn[i]
            j = arcs[e][0]
            
            if d[i] + 1 <= d[j] and flow[(j, i)]>0:
                d[j] = d[i] + 1
                pred[j] = i
                Q.append(j)
            
            while nextIn[e] > 0:
                e = nextIn[e]
                j = arcs[e][0]
                
                if d[i] + 1 <= d[j] and flow[(j, i)]>0:
                    d[j] = d[i] + 1   
                    pred[j] = i
                    Q.append(j)
            
        Q = Q[1:]
    
    return pred, d


##pre
    
import time

x, d, e, U = preprocess(source_node, target_node, nextOut, nextIn, U, fOut, fIn, arcs, arcs_dict)

N = dict(e)
N.pop(source_node)
N.pop(target_node)

while any(list(i> 0 for i in N.values())) == True:
    for i in N.keys():
        if e[i] > 0:
            x, e, d, U = push_relabel(i, e, x, d, U)
            N = dict(e)
            N.pop(source_node)
            N.pop(target_node)
            #print(e)

max_flow = e[target_node]
print(max_flow)