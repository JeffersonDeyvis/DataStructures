class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self._size = 0

    def empty(self):
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self._size == 0

    def push(self, element):
        if self.empty():
            node = Node(element)
            node.next = self.top
            self.top = node
        else:
            node = Node(element)
            node.next = self.top
            same_parity = int(node.value) % 2 == int(node.next.value) % 2
            if same_parity:
                node.value = abs(int(node.value) - int(node.next.value))
                self.top = node
            else:
                self.top = node
        self._size += 1

    def pop(self):
        """Remove and return the top element from the stack.

        Returns:
            The value of the removed element.

        Raises:
            IndexError: If the stack is empty.
        """
        is_empty = self.empty()
        if not is_empty:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.value

        raise IndexError("The stack is empty")

    def peek(self):
        """Return the top item from the stack without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        is_empty = self.empty()
        if not is_empty:
            return self.top.value
        raise IndexError("the stack is empty")

    def __repr__(self):
        """Return a string representation of the stack.

        Returns:
            str: A string representing the elements in the stack.
        """
        stack_representation = ""
        pointer = self.top
        while pointer:
            stack_representation += str(pointer.value) + "\n"
            pointer = pointer.next
        return stack_representation


stack = Stack()
for i in range(3, 0, -1):
    stack.push(i)

stack.push(7)
print(stack)







