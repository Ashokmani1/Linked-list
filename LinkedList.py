class LinkedList:
    def __init__(self):
        self.head = None
        
    def addToStart(self, data):
        # create a temporary node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    
    def addToEnd(self, data):
        start = self.head
        tempNode = Node(data)
        while start.getNextNode():
            start = start.getNextNode()
        start.setLink(tempNode)
        del tempNode
        return True

    # method displays Linked List
    def traverse(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()
        
        
    def remove(self, item):
        start = self.head
        previous = None
        found = False

        # search element in list
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()

        # if previous is None then the data is found at first position
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return found



# node class
class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    # method to set Link feild the Node
    def setLink(self, node):
        self.link = node

    # method returns data feild of the Node
    def getData(self):
        return self.data

    # method returns address of the next Node
    def getNextNode(self):
        return self.link


# main method

# creating LinkedList
print("creating LinkedList")
print()
myList = LinkedList()

# adding some elements to the start of LinkedList

myList.addToStart(5)
myList.addToStart(4)
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)

print("After Adding elements Linked List")
myList.traverse()

# adding some elements to the End of the LinkedList
myList.addToEnd(12)
myList.addToEnd(13)
myList.addToEnd(3)
myList.traverse()

print()
print("removing an element " + str(myList.remove(12)))
myList.traverse()
