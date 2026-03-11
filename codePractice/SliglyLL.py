class Node:
    """
    Represents a single node in the singly linked list.
    Each node has data and a pointer to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Manages the linked list, including operations like insertion, deletion,
    and traversal.
    """
    def __init__(self, head=None):
        self.head = head  # The head pointer, points to the first node

    def insert_at_beginning(self, data):
        """
        Inserts a new node at the beginning of the list. O(1) time complexity.
        """
        new_node = Node(data)
        new_node.next = self.head  # The new node points to the current head
        self.head = new_node     # Update the head to the new node

    def insert_at_end(self, data):
        """
        Inserts a new node at the end of the list. O(n) time complexity.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node  # The last node points to the new node

    def insert_after_node(self, previous_node, data):
        """
        Inserts a new node after a specific given node.
        """
        if previous_node is None:
            print("The previous node cannot be None")
            return
        new_node = Node(data)
        new_node.next = previous_node.next  # New node points to the next of previous node
        previous_node.next = new_node  # Previous node points to the new node

    def delete_node_by_value(self, key):
        """
        Deletes the first node found with the given value (key).
        """
        current_node = self.head
        previous_node = None

        # Case 1: Node to be deleted is the head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        # Case 2: Node to be deleted is not the head
        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next

        # If key was not present in the list
        if current_node is None:
            return

        # Unlink the node from the list
        previous_node.next = current_node.next
        current_node = None

    def search_node(self, key):
        """
        Searches for a node with the given value and returns it if found, else None.
        """
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return current_node
            current_node = current_node.next
        return None

    def print_list(self):
        """
        Traverses the list from the head and prints the data of each node.
        """
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Create a new singly linked list
myList = SinglyLinkedList()

# Insert elements
myList.insert_at_end(10)
myList.insert_at_beginning(5)
myList.insert_at_end(20)
myList.insert_at_beginning(3)

print("Created List:")
myList.print_list()

# Insert after a specific node - search if that node exist?
node_five = myList.search_node(5)
if node_five:
    myList.insert_after_node(node_five, 7)

print("\nList after inserting 7 after 5:")
myList.print_list()

# Delete a node
myList.delete_node_by_value(10)

print("\nList after deleting 10:")
myList.print_list()