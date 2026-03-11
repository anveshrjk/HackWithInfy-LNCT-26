class Node:
    """Represents a single node in a circular doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = self
        self.prev = self

class CircularDoublyLinkedList:
    """Implements the circular doubly linked list data structure."""
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        """Checks if the list is empty."""
        return self.head is None

    def insert_at_beg(self, data):
        """Inserts a new node at the beginning of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            last_node = self.head.prev
            new_node.next = self.head
            new_node.prev = last_node
            self.head.prev = new_node
            last_node.next = new_node
            self.head = new_node
        self.count += 1

    def insert_at_end(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            last_node = self.head.prev
            new_node.next = self.head
            new_node.prev = last_node
            last_node.next = new_node
            self.head.prev = new_node
        self.count += 1

    def delete(self, key):
        """Deletes the first occurrence of a node with the given key."""
        if self.is_empty():
            return

        current = self.head
        while True:
            if current.data == key:
                if self.count == 1:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                self.count -= 1
                return
            current = current.next
            if current == self.head:
                break
        print(f"Node with data {key} not found.")

    def display(self):
        """Prints the list from head to tail."""
        if self.is_empty():
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("HEAD")
        print(f"Total Nodes: {self.count}")

# Example Usage:
cdll = CircularDoublyLinkedList()
cdll.insert_at_beg(10)
cdll.insert_at_end(20)
cdll.insert_at_beg(5)
cdll.insert_at_end(30)
cdll.display()

cdll.delete(20)
cdll.display()

cdll.delete(5)
cdll.display()
