from queue import Queue
adj_list = {
    "a" : ["b","d"],
    "b" : ["a","c"],
    "c" : ["b"],
    "d" : ["a", "e", "f"],
    "e" : ["d", "f", "g"],
    "f" : ["d", "e" , "h"],
    "g" : ["e" , "h" ],
    "h" : ["g" , "f"],
}

visited = {}
level = {}
parent = {}
bfs_output = []

my_queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

# print(visited)
# print(level)
# print(parent)

source ="a"
visited[source] = True
level[source] = 0
my_queue.put(source)

# print(list(my_queue.queue))
while not my_queue.empty():
    u = my_queue.get() # pop the first element
    bfs_output.append(u)
    for x in adj_list[u]:
        if not visited[x]:
            visited[x] = True
            parent[x] = u
            level[x] = level[u]+1
            my_queue.put(x)

print(bfs_output)
print(level)


destination ="g"
path =[]
temp = destination
while temp is not None :
    path.append(temp)
    temp = parent[temp]
path.reverse()
print(path)
