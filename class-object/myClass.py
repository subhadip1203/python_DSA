class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

myObj = Node()
myObj.data = 10
print(myObj) 		# it will give only memory address 
print(myObj.data)	# it will be a value