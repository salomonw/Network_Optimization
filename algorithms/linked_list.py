
def read_linked_list(input_file):
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
                to_.append(int(val))
                u.append(int(dist))
            cnt += 1
    
    # Definig a data structure
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