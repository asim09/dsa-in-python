from node import Node


class LinkedList:
    

    def __init__(self):
        self.head = None
        self.length = 0
        
    def list_length(self):
        current = self.head
        count = 0
        while current !=None:
            count+=1
            current = current.getNext()
        return count

    def insert_node(self, data):     #add items in list
        newNode = Node()
        newNode.setData(data)

        if self.length==0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length+=1

    def print_list(self):
        current = self.head
        while current !=None:
            print(current.getData())
            current = current.getNext()

    def insert_at_end(self, data):
        newNode = Node()
        newNode.setData(data)
        current = self.head

        while current.getNext()!=None:
            current = current.getNext()
        current.setNext(newNode)
        self.length+=1

            
       
    
if __name__ == "__main__":

    ll = LinkedList()
    
    ll.insert_node(5)
    ll.insert_node(1)
    ll.insert_node(2)
    ll.insert_node(3)
    ll.insert_at_end(9)
    # print(ll.list_length())
    # ll.print_list()
    # ll.print_list()
    print(ll.list_length())




    
        
    