class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in edges:
            # print(start+'----'+end)
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def get_paths(self, start, visited={} , path=[]  ):
        if visited.get(start,False) != True and start  in self.graph_dict :
            visited[start]=True
            path.append(start)
            for next_node in self.graph_dict[start]:
                print(next_node)
                self.get_paths(next_node, visited, path)
        
        return path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    
route_graph = Graph(routes)
start = "Mumbai"
end = "New York"
print(route_graph.get_paths(start))