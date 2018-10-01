## Forward star graph representation
def forward_star(input_file):
    # read the text file and create two vectors with firstnode and endnode
    from_ = []
    to_ = []
    with open(input_file) as f:
        cnt = 0 
        for line in f: 
            if cnt == 0:
                (key, val) = line.split()
                num_nodes = (int(key)) 
                num_arcs = (int(val))
            else:
                (key, val) = line.split()
                from_.append(int(key)) 
                to_.append(int(val))

            cnt += 1

    adjacent_nodes = {}
    for node in range(num_nodes):
        adjacent_nodes[node+1] = []

    # look for all adhjacent nodes    
    for arc in range(len(from_)):
        adjacent_nodes[from_[arc]].append(to_[arc])

    endnode = []
    firstout = []
    pointer = 1
    firstout.append(1)

    for node in range(num_nodes):
        adjacent_nodes[node+1] = sorted(adjacent_nodes[node+1])
        endnode = endnode + adjacent_nodes[node+1]
        pointer  = pointer + len(adjacent_nodes[node+1])
        firstout = firstout + [pointer]

    #print(firstout)
    #print(endnode)
    return firstout, endnode