class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head = None
    
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


    def append(self,data):
        new_node = Node(data)
        
        if self.head ==None:
            self.head=new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next=new_node

    def insert_at_start(self,data):
        new_node = Node(data)
        if self.head ==None:
            self.append(new_node)
        else:
            new_node.next=self.head
            self.head=new_node
    
    def insert_at_position(self,data,position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_start(new_node)
        else:
            current_position = 0
            previous= None
            current = self.head
            while current_position <= position and current.next != None :
                if current_position == position:
                    new_node.next = current
                    current=new_node
                    previous.next =current
                    print(current_position)                    
                    break
                else:

                    current_position = current_position+1
                    previous =current
                    current=current.next

myLinkList = LinkedList()
myLinkList.print()
myLinkList.append(2)
myLinkList.append(3)
myLinkList.insert_at_start(1)
myLinkList.append(4)
myLinkList.insert_at_position(80,2)
myLinkList.print()