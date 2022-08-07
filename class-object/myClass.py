class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

myObj = Node()
myObj.data = 10


secondObj = Node()
secondObj.data=10
myObj.next = secondObj

print(myObj) 		# it will give only memory address 
print(myObj.data)	# it will be a value
print(myObj.next)	# it will give only memory address 
print(myObj.next.data)	# it will be a value
print(myObj.next.next)	# it will be a value