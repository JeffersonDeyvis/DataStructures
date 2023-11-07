from node import Node


class Stack:

    def __init__(self):
        """attributes : top and size"""
        self.top = None
        self._size = 0

    def stack_empty(self):
        return self._size == 0

    def stack_push(self, element):
        node = Node(element)
        node.next = self.top
        self.top = node
        self._size += 1

    def stack_pop(self):

        is_empty = self.stack_empty()
        if not is_empty:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.value

        raise IndexError("The stack is empty")
