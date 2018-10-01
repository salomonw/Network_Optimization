from time import time
def bellmanFord(input_file):
    # read graph
    firstout, endnode, dist, largest_dist = forward_star_dist(input_file)
    numNodes = len(firstout)-1
    numEdges = len(endnode)
    
    #initialize
    t0 = time()
    d = {}
    pred = {}
    d[0] = 99999999
    d[1] = 0 
    pred[0] = -1
    for k in range(numNodes-1):
        d[k+2] = 9999999999
    
    #algorithm
    for k0 in range(numNodes):
        k = k0+1
        for i0 in range(numNodes-1):
            i = i0+1
            for j0 in range(firstout[i-1], firstout[i]):
                j = endnode[j0-1]
                if d[i] + dist[j0-1] <= d[j]:
                    pred[j] = i
                    d[j] = d[i] + dist[j0-1]
    t1 = time()      
    print('-------------bellmanFord------------------')
    print(input_file)
    print('running time: ' + str(t1-t0))
    return d , t1-t0, pred