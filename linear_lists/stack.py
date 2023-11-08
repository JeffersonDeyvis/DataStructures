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
        node.previous = self.top
        self.top = node
        self._size += 1

    def stack_pop(self):
        is_empty = self.stack_empty()
        if not is_empty:
            node = self.top
            self.top = self.top.previous
            self._size -= 1
            return node.value

        raise IndexError("The stack is empty")

    def stack_peek(self):
        is_empty = self.stack_empty()
        if not is_empty:
            return self.top.value
        raise IndexError("the stack is empty")

    def __repr__(self):
        stack_representation = ""
        pointer = self.top
        while pointer:
            stack_representation += str(pointer.data) + "\n"
            pointer = pointer.previous
        return stack_representation
