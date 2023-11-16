""""
Module providing a doubly linked list data structure implementation in Python.

For more information on data structures and algorithms, consider
referring to SZWARCFITER, Jayme Luiz; MARKENZON, Lilian. Estruturas
de dados e seus algoritmos. 3.ed. Rio de Janeiro,
RJ: LTC, 2010. 302 p. ISBN 978-85-216-1750-1.
"""


class Node:
    def __init__(self, element):
        self.data = element
        self.previous = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def empty(self):
        """"
        """
        return self._size == 0

    def add_to_head(self, element):
        """"
        """
        node = Node(element)
        node.next = self.head

        if self.empty():
            self.head = node
            self.tail = node
            node.previous = None
            self._size += 1
        else:
            self.head.previous = node
            self.head = node
            node.previous = None
            self._size += 1

    def add_to_tail(self, element):
        """"
        """
        node = Node(element)
        node.previous = self.tail

        if self.empty():
            self.head = node
            self.tail = node
            node.next = None
            self._size += 1
        else:
            self.tail.next = node
            self.tail = node
            node.next = None
            self._size += 1

    def peep_the_head(self):
        if not self.empty():
            return self.head.data
        raise IndexError("The list is empty!")

    def peep_the_tail(self):
        if not self.empty():
            return self.tail.data
        raise IndexError("The list is empty!")

    def pop_head(self):
        if not self.empty():
            current = self.head
            current.next.previous = None
            self.head = current.next
            current.next = None
            self._size -= 1
            return current.data
        raise IndexError("the list is empty!")

    def pop_tail(self):
        if not self.empty():
            current = self.tail
            current.previous.next = None
            self.tail = current.previous
            current.previous = None
            self._size -= 1
            return current.data
        raise IndexError("The list is empty!")

