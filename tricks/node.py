class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


myNode = Node(10)
myNode.next = Node(11)
print(myNode)       # -- Memory address
print(myNode.data)  # -- a value
print(myNode.next)  # -- None or another Node
print(myNode.next.next)  # -- None or another Node