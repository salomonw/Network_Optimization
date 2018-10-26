# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 21:05:20 2018

@author: Salomon Wollenstein
"""

execfile('linked_list_assignment.py')
execfile('find_path.py')

## Dijkstra's with reduced costs
def dijkstra_linked_list(source_node, nextOut, nextIn, U, c, pi, fOut, fIn, arcs, flow):
    numNodes = len(fIn)
    numEdges = len(U)
      
    Q = []
    pred = {}
    d ={}
    
    for k in range(numNodes):
        d[k+1] = 1000000
    
    d[source_node] = 0
    Q.append(source_node)
    
    while len(Q) > 0:

        i = Q[0]
        
        if fOut[i] > 0:
            e = fOut[i] 
            j = arcs[e][1]

            if d[i] + pi[i] - pi[j] <= d[j]  and U[(i,j)] > 0:
                d[j] = d[i] +  c[(i, j)] + pi[i] - pi[j]
                pred[j] = i
                Q.append(j)
            
            while nextOut[e] > 0:             
                e = nextOut[e]
                j = arcs[e][1]

                if  d[i] + c[(i, j)] + pi[i] - pi[j] <= d[j] and U[(i,j)] > 0:
                    d[j] = d[i] + c[(i, j)] + pi[i] - pi[j]
                    pred[j] = i
                    Q.append(j)
                    
        elif fIn[i] > 0:
            e = fIn[i]
            j = arcs[e][0]
            
            if d[i] -  (c[(j, i)] + pi[j] - pi[i]) <= d[j]  and flow[(j, i)] > 0:
                d[j] = d[i] -(c[(j, i)] + pi[j] - pi[i])
                pred[j] = i
                Q.append(j)
                
            while nextIn[e] > 0:
                e = nextIn[e]
                j = arcs[e][0]
                
                if d[i] - (c[(j, i)] + pi[j] - pi[i]) <= d[j] and flow[(j, i)] > 0:               
                    d[j] = d[i] - (c[(j, i)] + pi[j] - pi[i])
                    pred[j] = i
                    Q.append(j)

        Q = Q[1:]
    
    return pred, d



input_file = '../min_cost_data/saloassign.txt'

source_node = 1

# Reading file
nextOut, nextIn, x, U_, fOut, fIn, arcs = read_linked_list_assignment2(input_file)
arcs_dict = {str(v): k for k, v in arcs.items()}

max_flow = 0

# Generating source and sink for the assignment problem
c = {}
x = {}
rc = {}
U = {}
for k in arcs.keys():
    x[(arcs[k][0], arcs[k][1])] = 0
    c[(arcs[k][0], arcs[k][1])] = U_[k]
    rc[(arcs[k][0], arcs[k][1])] = U_[k]
    U[(arcs[k][0], arcs[k][1])] = 1

pi = {}
e = {}
b = {}

num_nodes = len(fIn)
e[1] = num_nodes/2-1
e[num_nodes] = -num_nodes/2-1
for i in range(num_nodes):
    pi[i+1] = 999
    if i+1 <= num_nodes/2:
        b[i+1] = 0
        e[i+1] = 0
        pi[i+1] = 0
    else:
        b[i+1] = 0
        e[i+1] = 0
        k = fIn[i+1] 
        
        while k > 0:
            j = arcs[k][0]
            pi[i+1] =0
            k = nextIn[k]

e[1] = num_nodes/2-1
e[num_nodes] = -num_nodes/2+1

# Setting sets of nodes with positive and negative excess
E = []
D = []
for i in e.keys():
    if e[i] > 0:
        E.append(i)
    if e[i] < 0:
        D.append(i)
    
import random



# Starting the iteration
P = {}
while len(E) > 0:
    k = random.choice(E)
    l = random.choice(D)
    # Calculating distances with respect to the reduced costs
    pred, d = dijkstra_linked_list(k, nextOut, nextIn, U, c, pi, fOut, fIn, arcs, x)

    path = find_path(k, l, pred, d)
 
    # Updating the dual variables 
    for t in pi.keys():
        pi[t] = pi[t] - d[t]


    
    U_minPath = []
    X_minPath = []
    
    arcs_in_path = [[path[i], path[i+1]] for i in range(len(path[:-1]))]
    print(arcs_in_path)

    # Calculating the augmentation size in for that path
    for i in arcs_in_path:
       s = i[0]
       t = i[1]
       if [s, t] in arcs.values():
           U_minPath.append(U[(s,t)])
       else:
           X_minPath.append(x[(t,s)])
    
    U_minPath.append(i for i in X_minPath)
    u_minPath = min(U_minPath)
    delta = min(e[k] , -e[l], u_minPath)

    # Updateing the flow x, capacity U, excess e
    for i in arcs_in_path:
       s = i[0]
       t = i[1]

       if [s, t] in arcs.values():
           x[(s,t)] = x[(s,t)] + delta
           U[(s,t)] = U[(s,t)] - delta
           e[s] = e[s] - delta
           e[t] = e[t] + delta

       else:
           pause()
           
           x[(s,t)] = x[(s,t)] - delta
           U[(s,t)] = U[(s,t)] + delta
    
           e[s] = e[s] + delta
           e[t] = e[t] - delta


    # Updating reduced costs
    for a in arcs.values():
        rc[(a[0], a[1])] = c[a[0],a[1]] - pi[a[0]] + pi[a[1]]
        
    # Updating the set E and D
    E = []
    D = []
    for i in e.keys():
        if e[i] > 0:
            E.append(i)
        if e[i] < 0:
            D.append(i)
  
  #  print('------------------')
  #  print('k = ' + str(k) + ', l = ' + str(l))
  #  print('pi = ' + str(pi.values() ))
  #  print('d = ' + str(d.values() ))
  #  print('rc = ' + str(rc.keys() ))
  #  print('rc = ' + str(rc.values() ))
  #  print('x = ' + str(x.values()))
  #  print('e = ' + str(e.values()) )  
    
# Print results
min_cost = 0
for (i, j) in x.keys():
    min_cost += x[(i, j)] * c[(i, j)]
print('min-cost is: ' + str(min_cost))