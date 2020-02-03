import copy
class DoublyLinkedList:
    class _Node:
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._trailer
        self._head = self._header
        self._tail = self._trailer
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def add_to_list(self, e):
        newnode = self._Node(e, self._tail, self._head)
        self._head._next = newnode
        self._tail._prev = newnode
        self._head = newnode
        self._size += 1

    def _swap_nodes(self, node1, node2):
        swaplist = self
        before_node1 = node1._prev
        after_node1 = node1._next
        before_node2 = node2._prev
        after_node2 = node2._next

        before_node1._next = node2
        node2._prev = before_node1
        node2._next = after_node1
        after_node1._prev = node2

        before_node2._next = node1
        node1._prev = before_node2
        node1._next = after_node2
        after_node2._prev = node1
        print('Swapped {} and {}'.format(node1._element, node2._element))
        return

    def bubble_sort(self):
        node1 = self._header._next

        while node1._next is not self._trailer:
            node2 = node1._next
            while node2 is not self._trailer:
                if node1._element > node2._element:
                    temp = node1._element
                    node1._element = node2._element
                    node2._element = temp
                    print('Swapped {} and {}'.format(node1._element, node2._element))
                    self.print()
                node2 = node2._next
            node1 = node1._next

    def print(self):
        elements = []
        node = self._header._next
        while node is not self._trailer:
            elements.append(node._element)
            node = node._next
        print(elements)

dll = DoublyLinkedList()
dll.add_to_list(4)
dll.add_to_list(2)
dll.add_to_list(3)
dll.add_to_list(5)
dll.add_to_list(1)
dll.print()
dll.bubble_sort()