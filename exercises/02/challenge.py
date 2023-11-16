""""
implementar uma lista ligada e realizar
algumas operações utilizando a notação poloneza
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
        


