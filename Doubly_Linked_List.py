class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None

    def printDLL(self):
        current=self.head
        while current!=None:
            print(current.data,end=" ")
            current=current.next

    def insertAtStart(self,data):
         newNode=Node(data)
         if self.head is None :
             self.head=newNode
             self.tail=newNode
         else:
             self.head.prev = newNode
             newNode.next=self.head
             self.head=newNode

    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode

    def Delete(self,key):
        current = self.head
        if self.head is not None :                  #chack is empty
            if current.data == key :                # ths if for delete the first node
                current.next.prev = None
                self.head = self.head.next
                current.head=None
                current = None
            else:                                   # not the first node
                while current.next is not  None :
                    if(current.data == key):
                        break
                    current=current.next
                if current.next :                   #chack if it the middle
                     current.prev.next = current.next
                     current.next.prev = current.prev
                     current.next = None
                     current.prev = None
                     current=None
                else:                               #if it's the end
                     if current.data == key :       #if the last node is the key
                         self.tail.prev.next = None
                         self.tail.next = None

                     else:                          #if the key is not in the list
                         print()
                         print("The number you enter is not in the linked list !!!!")

        else:
            print("You are deleting from empty linked list")


L=DoublyLinkedList()
L.insertAtStart(3)
L.insertAtStart(2)
L.insertAtStart(1)
L.printDLL()
L.insertAtEnd(4)
L.insertAtEnd(5)
print()
L.printDLL()
L.Delete(5)
print()
L.printDLL()