def find_path(node, pred, d):
    path = []
    k = node
    while k > 1 :
        path.append(k)
        k = pred[k]
    path.append(1)

    print('Shortest path from 1 to ' + str(node) + ' is: ')
    print(path)
    print('and its distance is = ' + str(d[node]))
    return path