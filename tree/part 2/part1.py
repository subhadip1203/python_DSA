class BST():
  def __init__(self,data) :
      self.left =None
      self.right=None
      self.data=data

  def insert(self,data):
    if self.data > data :
      if self.left:
        self.left.insert(data)
      else:
        self.left = BST(data)

    elif self.data < data:
      if self.right:
        self.right.insert(data)
      else:
        self.right=BST(data)
    else:
      return 
    
  

  def print(self):

    #go for all the left recursively
    if self.left:
      self.left.print()
    
    print(self.data, end =" ")

    #go for all the right recursively
    if self.right:
      self.right.print()


mytree = BST(6)
mytree.insert(10)
mytree.insert(3)
mytree.insert(6)
mytree.insert(1)
mytree.insert(23)

mytree.print()