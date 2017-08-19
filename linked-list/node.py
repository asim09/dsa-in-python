## Node of a Singly Linked List

class Node(object):
    
    def __init__(self):
        self.data = None
        self.next = None

    #Method for setting data field of Node

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    #Method for setting next field of Node

    def setNext(self, next):
        self.next = next

    #Method for getting next field of Node

    def getNext(self):
        return self.next

    # Returns true if node points to another point

    def hasNext(self):
        return self.next!= None

