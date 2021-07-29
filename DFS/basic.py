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

status = {} # each node "notVisited" , "exploring" , "explored"
parent = {}
step = {} # for each node [startStep , EndStep] 
DFS_result =[]

for node in adj_list.keys():
    status[node] = "notVisited"
    parent[node] = None
    step[node] = [-1,-1]
# print(status)
# print(step)
# print(parent)

stepNow = 0
def DFS_utils(source):
    global stepNow
    status[source] = "exploring"
    step[source][0] = stepNow 
    DFS_result.append(source)
    stepNow +=1
    for branch in adj_list[source]:
        if status[branch] == "notVisited":
            parent[branch] = source
            DFS_utils(branch)
    
    status[source] = "explored" 
    step[source][1] = stepNow  
    stepNow +=1  

DFS_utils("a")
print(DFS_result)
print(step)
print(parent)   

