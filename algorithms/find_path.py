def find_path(source_node, target_node, pred, d):
    path = []
    k = target_node
    while k != source_node :
        path.append(k)
        k = pred[k]
    path.append(source_node)

    path = list(reversed(path))
    #print('Shortest path from 1 to ' + str(target_node) + ' is: ')
    #print(path)
    #print('and its distance is = ' + str(d[target_node]))
    return path
