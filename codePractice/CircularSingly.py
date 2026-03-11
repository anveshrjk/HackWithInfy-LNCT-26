class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    """Represents the circular linked list structure."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head # Points to itself if it's the only node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head # New last node points back to head

    def display(self):
        """Prints all the elements in the list."""
        if not self.head:
            print("The list is empty.")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("...") # Indicates the loop back to the start

# Example Usage:
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.display()
