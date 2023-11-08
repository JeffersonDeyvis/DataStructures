"""Module providing a stack data structure implementation in Python.

For more information on data structures and algorithms, consider referring to
SZWARCFITER, Jayme Luiz; MARKENZON, Lilian. Estruturas de dados e seus algoritmos.
3.ed. Rio de Janeiro, RJ: LTC, 2010. 302 p. ISBN 978-85-216-1750-1.
"""
from linear_lists.node import Node


class Stack:
    """Class representing a stack data structure.

    The stack follows the Last In, First Out (LIFO) principle.
    """

    def __init__(self):
        """Initialize an empty stack.

        The stack is represented using the attributes top and size.
        The top attribute points to the top element of the stack.
        The size attribute keeps track of the number of elements in the stack.
        """
        self.top = None
        self._size = 0

    def empty(self):
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self._size == 0

    def push(self, element):
        """Add an element to the top of the stack.
        """
        node = Node(element)
        node.next = self.top
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
