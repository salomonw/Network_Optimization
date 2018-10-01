# Testing different algorithms and printing results 
execfile('load_functions.py')

net_dir = 'networks/'
net_file = 'smallnet.txt'
net_path = net_dir + net_file

d , time_, pred = dijkstra(net_path)
path =  find_path(5, pred, d)
path =  find_path(10, pred, d)

d, time_, pred = bellmanFord(net_path)
path =  find_path(5, pred, d)
path =  find_path(10, pred, d)

d, time_, pred = bellmanFordQueue(net_path)
path =  find_path(5, pred, d)
path =  find_path(10, pred, d)
