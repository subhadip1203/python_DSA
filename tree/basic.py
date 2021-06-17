class Node:
    def __init__(self, data):        
        self.head = None
        self.data = data
        self.level = 0
        self.children=[]

    def addChild(self,data):
        self.children.append(data)
        data.head = self
        data.level=self.level+1

    def print(self):
        space = '  '*self.level+' '
        hyphen= '|-'
        print(space+hyphen+str(self.data))
        
        if self.children:
            for c in self.children:
                c.print()
    
rootNode = Node(0)

base1_1= Node(1)
base1_2= Node(2)
base1_3= Node(3)
rootNode.addChild(base1_1)
rootNode.addChild(base1_2)
rootNode.addChild(base1_3)

base2_4= Node(4)
base2_5= Node(5)
base1_1.addChild(base2_4)
base1_1.addChild(base2_5)

rootNode.print()