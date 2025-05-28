class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insert_at_beginning(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

# Create nodes
ll = LinkedList()
ll.head = Node("Toyota")
l2 = Node("BMW")
l3 = Node("Audi")
l4 = Node("Lamborghini")

# Link the nodes
ll.head.next = l2
l2.next = l3
l3.next = l4

#insert a new node at the beginning
ll.insert_at_beginning("Ford")

# Print the linked list
ll.listprint()



