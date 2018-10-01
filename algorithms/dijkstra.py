from time import time

## Dijkstra's Algorithm
def dijkstra(input_file):
    # read graph
    firstout, endnode, dist, largest_dist = forward_star_dist(input_file)
    numNodes = len(firstout) - 1
    numEdges = len(endnode)
    t0 = time()
    # initialize 
    Q = []
    d = {}
    pred = {}
    d[0] = 99999999
    d[1] = 0 
    pred[0] = -1
    for k in range(numNodes-1):
        d[k+2] = 9999999999
    Q.append(1)

    # algorithm
    while len(Q)>0:
        for i in range(firstout[Q[0]-1], firstout[Q[0]]):
            j = Q[0]
            k = endnode[i-1]
            if d[j] + dist[i-1] <= d[k]:
                pred[k] = j
                d[k] = d[j] + dist[i-1]
                Q.append(k)
        #print(Q)
        Q = Q[1:]
    t1 = time()
    print('--------------dijkstra-----------------')
    print(input_file)
    print('running time: ' + str(t1-t0))
    return d, t1-t0, pred