from unittest import TestCase
from linear_lists.dll import DoublyLinkedList


class TestDoublyLinkedList(TestCase):
    def test_doubly_linked_list_empty(self):
        dll = DoublyLinkedList()
        self.assertTrue(True == dll.empty())

    def test_add_to_head(self):
        dll = DoublyLinkedList()
        for i in range(2):
            dll.add_to_head(i)

        self.assertTrue(dll.peep_the_head() == 1)
        self.assertTrue(dll.peep_the_tail() == 0)

