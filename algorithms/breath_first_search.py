## Breath first search Alg
#select a starting node
def BFS(num_nodes, from_, to_):
    s = from_[0]
    print(s)
    visited_nodes = [False] * num_nodes
    queue = []
    nodes = []
    queue.append(s)
    nodes.append(s)
    while queue:
        s = queue.pop(0)
        cnt = 0
        for i in from_:
            if i == s:
                if not to_[cnt] in nodes:
              #      print(str(i) + ' -> ' + str(to_[cnt]))
                    visited_nodes[to_[cnt]-1] = True
                    nodes.append(to_[cnt])
                    queue.append(to_[cnt])
            cnt += 1 

    return nodes
  #  print(nodes)

#BFS(num_nodes, from_, to_)