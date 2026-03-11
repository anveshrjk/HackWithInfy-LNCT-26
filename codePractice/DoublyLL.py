class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Points to the first node
        self.tail = None  # Points to the last node (optional, but efficient)

    def append(self, data):
        """Adds a new node to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        # This implementation uses a tail pointer for O(1) appending

    def prepend(self, data):
        """Adds a new node to the beginning of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        # This operation has a time complexity of O(1)

    def delete_by_value(self, value):
        """Deletes the first occurrence of a node with the given value."""
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # Node to be deleted is the head

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # Node to be deleted is the tail
                return
            current = current.next

    def display_forward(self):
        """Traverses and prints the list from head to tail."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        """Traverses and prints the list from tail to head."""
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Create a new doubly linked list
dll = DoublyLinkedList()

# Append elements
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Forward traversal after appending:")
dll.display_forward()

# Prepend an element
dll.prepend(0)

print("Forward traversal after prepending:")
dll.display_forward()

# Delete a node by value
dll.delete_by_value(2)

print("Forward traversal after deleting 2:")
dll.display_forward()

print("Backward traversal:")
dll.display_backward()

