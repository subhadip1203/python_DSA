class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    



class Graph:
    def __init__(self,routes):
        self.graph_dict={}
        for start,end in routes:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        # print("graph data :",self.graph_dict)

    def paths(self,start,end,path=[]):
        trailing_path = path+[start]
        print(trailing_path)
        if start==end:
            return [trailing_path]
        else:
            temp_path=[]
            if start in self.graph_dict:                
                for next in self.graph_dict:
                    print("--------- Loop start -------------")
                    if next not in trailing_path:
                        return_data = self.paths(next,end,trailing_path)
                        print(bcolors.OKGREEN ,"return data: ",return_data ,bcolors.ENDC )
                        for p in return_data:
                            temp_path.append(p)
                    else:
                        print(bcolors.FAIL ,next ,"is in :",trailing_path,bcolors.ENDC )
                    print("--------- Loop ends -------------")
            print("----------- end of step -------------")
            return temp_path




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
print(route_graph.paths(start,end))