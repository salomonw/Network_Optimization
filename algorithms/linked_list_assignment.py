# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:38:59 2018

@author: Salomon Wollenstein
"""


def read_linked_list_assignment(input_file):
        # read the text file and create two vectors
    from_ = []
    to_ = []
    u = []
    with open(input_file) as f:
        cnt = 0 
        for line in f: 
            if cnt == 0:
                (key, val, dist) = line.split()
                num_nodes = (int(key)) 
                num_arcs = (int(val))
                largest_dist = (int(dist))
            else:
                (key, val, dist) = line.split()
                from_.append(int(key)) 
                to_.append(int(val) + num_nodes)
                u.append(int(dist))
            cnt += 1

    num_arcs = len(from_)
    # Definig a data structure
    num_nodes = num_nodes*2
    nextOut = {}
    nextIn = {}
    flow = {}
    U = {}
    fOut = {}
    fIn = {}
    arcs = {}
    for l in range(num_arcs):
        k = l +1 
        nextOut[k] = -1
        nextIn[k] = -1
        flow[k] = 0
        U[k] = 0
        
    for l in range(num_nodes):
        k = l + 1
        fOut[k] = -1
        fIn[k] = -1
    
    # Asigningnetwork data to structure
    for l in range(num_arcs):
        k = l +1 
        i = from_[l]
        j = to_[l]
        U[k] = u[l]
        nextOut[k] = fOut[i]
        fOut[i] = k
        nextIn[k] = fIn[j]
        fIn[j] = k
        arcs[k] = [i, j] 
        
    return nextOut, nextIn, flow, U, fOut, fIn, arcs


#input_file = 'smallflow.txt'
    




def read_linked_list_assignment2(input_file):
        # read the text file and create two vectors
    from_ = []
    to_ = []
    u = []
    with open(input_file) as f:
        cnt = 0 
        for line in f: 
            if cnt == 0:
                (key, val, dist) = line.split()
                num_nodes = (int(key)) 
                num_arcs = (int(val))
                largest_dist = (int(dist))
            else:
                (key, val, dist) = line.split()
                from_.append(int(key)+1) 
                to_.append(int(val) + num_nodes + 1)
                u.append(int(dist))
            cnt += 1
            
    from_2 = list(from_)
    for j in range(num_nodes):
        i = j + 2
        from_.append(1)
        to_.append(i)
        u.append(0)
        
    to_2 = list(to_)
    max_ = max(max(from_2), max(to_2))
    for j in range(num_nodes):
        i = num_nodes+2+j
        from_.append(i)
        to_.append(max_ + 1)
        u.append(0)
       
    num_arcs = len(from_)
    # Definig a data structure
    num_nodes = num_nodes*2 + 2
    nextOut = {}
    nextIn = {}
    flow = {}
    U = {}
    fOut = {}
    fIn = {}
    arcs = {}
    for l in range(num_arcs):
        k = l +1 
        nextOut[k] = -1
        nextIn[k] = -1
        flow[k] = 0
        U[k] = 0
        
    for l in range(num_nodes):
        k = l + 1
        fOut[k] = -1
        fIn[k] = -1
    
    # Asigningnetwork data to structure
    for l in range(num_arcs):
        k = l +1 
        i = from_[l]
        j = to_[l]
        U[k] = u[l]
        nextOut[k] = fOut[i]
        fOut[i] = k
        nextIn[k] = fIn[j]
        fIn[j] = k
        arcs[k] = [i, j] 
        
    return nextOut, nextIn, flow, U, fOut, fIn, arcs


#input_file = 'smallflow.txt'