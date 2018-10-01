from time import time
def bellmanFordQueue(input_file):
    # read graph
    firstout, endnode, dist, largest_dist = forward_star_dist(input_file)
    numNodes = len(firstout)-1
    numEdges = len(endnode)
    t0 = time()
    
    #initialize
    Q = []
    in_Q = {}
    d = {}
    pred = {}
    d[0] = 99999999
    d[1] = 0 
    pred[0] = -1
    for k in range(numNodes-1):
        d[k+2] = 9999999999
        in_Q[k+2] = 0
    Q.append(1)
    #in_Q[1] = 1
    
    #algorithm
    while len(Q)>0:
        k = Q[0]
        for j0 in range(firstout[k-1]-1, firstout[k]): 
            j = endnode[j0-1]
            if d[k] + dist[j0-1] <= d[j]:
                pred[j] = k
                d[j] = d[k] + dist[j0-1]
                #.append(j)
                if j not in Q:
                    Q.append(j)
        Q = Q[1:]
    t1 = time()  

    print('-------------bellmanFordQueue------------------')
    print(input_file)
    print('running time: ' + str(t1-t0))
    return d , t1-t0, pred