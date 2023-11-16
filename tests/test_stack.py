from unittest import TestCase
from linear_lists.stack import Stack


class TestStack(TestCase):

    def test_stack_empty(self):
        stack = Stack()
        self.assertTrue(True == stack.empty())

    def test_stack_peek(self):
        stack = Stack()
        stack.push(2)
        self.assertTrue(2 == stack.peek())

    def test_stack_push(self):
        stack = Stack()
        for i in range(3):
            stack.push(i)

        stack_check = "2" + "\n" + "1" + "\n" + "0" + "\n"
        self.assertTrue(stack_check == str(stack))

    def test_stack_pop(self):
        stack = Stack()
        for i in range(3):
            stack.push(i)

        stack.pop()
        stack.pop()
        stack_check = "0" + "\n"
        self.assertTrue(stack_check == str(stack))
