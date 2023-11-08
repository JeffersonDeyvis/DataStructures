"""Module providing a queue data structure implementation in Python.

For more information on data structures and algorithms, consider referring to
SZWARCFITER, Jayme Luiz; MARKENZON, Lilian. Estruturas de dados e seus algoritmos.
3.ed. Rio de Janeiro, RJ: LTC, 2010. 302 p. ISBN 978-85-216-1750-1.
"""
from linear_lists.node import Node


class Queue:
    """Class representing a queue data structure.

    The queue follows the First In, First Out (FIFO) principle.
    """

    def __init__(self):
        """Initialize an empty queue.

        The queue is represented using the attributes front, back and size.
        The front attribute points to the first element of the queue.
        The back attribute points to the last element of the queue.
        The size attribute keeps track of the number of elements in the queue.
        """
        self.front = None
        self.back = None
        self._size = 0

    def empty(self):
        """Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self._size == 0

    def push(self, element):
        """Add an element to the end of the queue.
        """
        node = Node(element)
        if self.back is None:
            self.back = node
        else:
            self.back.next = node
            self.back = node

        if self.front is None:
            self.front = node

        self._size += 1

    def pop(self):
        """Remove and return the first element in the queue.

        Returns:
            The value of the removed element.

        Raises:
            IndexError: If no one has joined the queue yet.
        """
        is_empty = self.empty()
        if not is_empty:
            node = self.front
            self.front = self.front.next
            self._size -= 1
            return node.value

        raise IndexError("no one has joined the queue yet!")

    def peek(self):
        """Return the first item of the queue without removing it.

        Raises:
            IndexError: If no one has joined the queue yet.
        """
        is_empty = self.empty()
        if not is_empty:
            node = self.front
            return node.value

        raise IndexError("no one has joined the queue yet!")

    def __repr__(self):
        """Return a string representation of the queue.

        Returns:
            str: A string representing the elements in the queue.
        """
        queue_representation = ""
        pointer = self.front
        while pointer:
            queue_representation += str(pointer.value) + " - "
            pointer = pointer.next
        return queue_representation
