class Node ():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class QueueDll():
    def __init__(self):
        self.head = None
        self.tail = None

    def printQue(self):
        if self.head == None:
            print("the Queue is empty !! ",end=" ")
        else:
           current=self.head
           while current!=None:
              print(current.data,end=" ")
              current=current.next

    def enQueue(self,data):
        newNode = Node(data)
        if self.head is None:
            self.tail=newNode
            self.head=newNode
            print("you enQueue this data to the Queue : ", data)
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail=newNode
            print("you enQueue this data to the Queue : ", data)

    def deQueue (self):
        if self.head is None :
            print("The Queue is empty !!",end=" ")
        else:
            if self.head.next is None:
                print("you deQueue this data from the Queue : ", self.head.data)
                self.head=None
                self.tail=None
            else:
               print("you deQueue this data from the Queue : ",self.head.data)
               self.head = self.head.next
               self.head.prev = None

queue=QueueDll()
queue.printQue()
print()
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.enQueue(4)
queue.printQue()
print()
queue.deQueue()
print()
queue.deQueue()
print()
queue.deQueue()
print()
queue.deQueue()
print()
queue.deQueue()