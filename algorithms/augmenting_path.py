# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:32:31 2018

@author: Salomon
"""

execfile('linked_list.py')
execfile('find_path.py')

# Augmenting path 
input_file = '../max_flow_data/medflow.txt'

source_node = 1
target_node = 300

nextOut, nextIn, flow, U, fOut, fIn, arcs = read_linked_list(input_file)
arcs_dict = {str(v): k for k, v in arcs.items()}


max_flow = 0
## Dijkstra's
def dijkstra_linked_list(source_node, target_node, nextOut, nextIn, U, fOut, fIn, arcs):
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
            
            if d[i] + 1 <= d[j] and flow[e]>0:
                d[j] = d[i] + 1
                pred[j] = i
                Q.append(j)
            
            while nextIn[e] > 0:
                e = nextIn[e]
                j = arcs[e][0]
                
                if d[i] + 1 <= d[j] and flow[e]>0:
                    d[j] = d[i] + 1   
                    pred[j] = i
                    Q.append(j)
            
        Q = Q[1:]
    
    return pred, d


x=1
while x>0:
    #print(1)
    ## shortest path problem
    pred, d = dijkstra_linked_list(source_node, target_node, nextOut, nextIn, U, fOut, fIn, arcs)
    ## find shortest path
    try:
        path = find_path(source_node, target_node, pred, d)
    except:
        break
        x = -1
    
    
    arcs_in_path = [arcs_dict[str([path[i], path[i+1]])] for i in range(len(path[:-1]))]

    ## Augment under that path
    augment_size = min(U[i] for i in arcs_in_path)
    max_flow += augment_size
    print('augmentation in: '+ str(path) + ' of size: ' + str(augment_size))
    ## update capacities and flows
    for i in arcs_in_path:
       flow[i] += augment_size 
       U[i] = U[i] - augment_size


## find the max flow
j =  fIn[target_node]
while j > 0:
    max_flow += flow[j]
    j = nextIn[j]


#print(flow)
print('max-flow is: ' + str(max_flow/2))