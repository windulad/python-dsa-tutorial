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
    
    # Implement add (add from front) node to Linked List
    def add(self, data):
        new_node = Node(data)       # Create a new Node
        new_node.next_node = self.head      # Pointer of new Node to Head of previous Linked List 
        self.head = new_node        # Pointer to new Linked List

    # Implement search to Linked List
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    # Implement insert to Linked List
    def insert(self, data, index):
        # Add index 0 node to front of Linked List
        if index == 0:
            self.add(data)

        # Insert index != 0 to Linked List
        if index > 0:
            new = Node(data)        # Create new Node

            position = index        # Assign index to position
            current = self.head

            while position > 1:
                current = current.next_node        # Traverse through Linked List from Head to Tail until index found
                position -= 1

            prev_node = current             # Assign current node in index to previous
            next_node = current.next_node   # Assign next node in index to next

            prev_node.next_node = new       # Assign next node of previous as new node
            new.next_node = next_node       # Assign next node of new node as next node

    # Implement delete to Linked List
    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            # If key is head
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node       # Delete head and assign to next node
            # If key is not head
            elif current.data == key:
                found = True
                previous.next_node = current.next_node      # Delete current node and assign pointer to next node
            else:
                previous = current
                current = current.next_node
        return current

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

# L = LinkedList()
# L.add(1)
# L.add(2)
# L.add(3)
# print(L)

# L = LinkedList()
# L.add(10)
# L.add(2)
# L.add(45)
# L.add(15)
# n = L.search(44)
# print(n)

L = LinkedList()
L.add(10)
L.add(2)
L.add(45)
L.add(15)
L.add(67)
print(L)
L.remove(2)
print(L)