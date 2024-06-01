# Implementation of Node
class Node:
    data = None     # Define data of a Node
    next_node = None        # Define pointer to the Next Node

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
# Implementation of Linked List
class LinkedList:
    # Implement an empty Linked List
    def __init__(self):
        self.head = None

    # Check whether Linked List is empty
    def is_empty(self):
        return self.head == None

    # Return number of Nodes in the Linked List
    def size(self):
        current = self.head     # Initial Node is head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    # Implement add node to Linked List
    def add(self, data):
        new_node = Node(data)       # Create a new Node
        new_node.next_node = self.head      # Pointer of new Node to Head of previous Linked List 
        self.head = new_node        # Pointer to new Linked List

    # Implement representing method for the Linked List
    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current == self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node == None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node

        return '->'.join(nodes)















# N1 = Node(10)
# print(N1)
# N2 = Node(20)
# N1.next_node = N2
# print(N1.next_node)

# L = LinkedList()
# N1 = Node(10)
# L.head = N1
# print(L.size())

L = LinkedList()
L.add(1)
L.add(2)
L.add(3)
print(L)