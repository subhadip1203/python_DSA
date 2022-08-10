class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addItems(self,value):
        current = self.head
        if current == None:
            current = Node(value)
        else:
            while current.next != None:
                current = current.next
            current.next = Node(value)

    def print(self):
        print
        print("Start", end =" ")
        if self.head == None:
            print("-> No data", end =" ")
        else:
            current= self.head
            while current.next != None:
                print('->'+str(current.data), end =" " )
                current=current.next
            print('->'+str(current.data), end =" " )
        print("")


myArr = [1,2,3,4,5]
myLinkedList = LinkedList()
for x in myArr:
    myLinkedList.addItems(x)
myLinkedList.print()

