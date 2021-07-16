class Node ():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class StackDll():
    def __init__(self):
        self.head=None
        self.tail=None

    def printDLL(self):
        if self.tail == None:
            print("The stack is empty !! ")
        else:
            current=self.tail
            while current!=None:
               print(current.data,end=" ")
               current=current.prev

    def push(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head=newNode
            self.tail=newNode
            print("you push this data to the stack : ", data)
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            print("you push this data to the stack : " , data)

    def pop(self):
        if self.head is None:
            print("The stack is empty !!")
        else:
            if  self.tail.prev is None:
                print("you pop this data from the stak : ", self.head.data)
                self.head=None
                self.tail = None


            else:
                print("you pop this data from the stak : ",self.head.data)
                self.head.next.prev = None
                self.head = self.head.next




stack=StackDll()
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(0)
stack.printDLL()
print()
stack.pop()
stack.printDLL()
print()
stack.pop()
stack.printDLL()
print()
stack.pop()
stack.printDLL()
print()
stack.pop()
stack.printDLL()
print()
stack.pop()

