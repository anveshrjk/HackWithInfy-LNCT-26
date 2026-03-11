class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        """Add an item to the top of the stack."""
        self.stack.append(element)

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        """Get the value of the top item in the stack without removing it."""
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Get the number of items in the stack."""
        return len(self.stack)

stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
print(stk.size())
print(stk.peek())