'''
  ListNode : each Node
  each node will have :
    val
    next : default value is None
'''
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


'''
  LinkedList: full list of Nodes
'''
class LinkedList:
  def __init__ (self):
    self.head = None

  '''
  current : pointer => default value : None
  '''
  def addItems(self , arr):
    current = None
    for i in arr:
      if current == None:
        self.head = ListNode(i)
        current = self.head
      else:
        current.next = ListNode(i)
        current = current.next

  def print(self):
    p = self.head
    print('Head', end =" " )
    while p != None :
      print('->'+str(p.val), end =" " )
      p = p.next   
    print()

  def reverse(self):
    next , prev , current = None , None , self.head
    while current :
      next = current.next
      current.next = prev 
      prev , current = current , next # for next step , current will be prev and , next will be current
    self.head = prev
    
head = [1,2,3,4,5,6]
myList = LinkedList()
myList.addItems(head)
myList.print()
myList.reverse()
myList.print()