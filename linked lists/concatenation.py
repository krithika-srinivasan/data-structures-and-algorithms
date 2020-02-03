class LinkedList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = self._Node(None, None)
        self._tail = self._Node(None, None)
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def add_to_list(self, e):
        newnode = self._Node(e, None)
        if self.is_empty():
            self._head = newnode
        else:
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1

    def head(self):
        return self._head

    def print(self):
        elements = []
        node = self._head
        while node is not None:
            elements.append(node._element)
            node = node._next
        print(elements)


def concatenate(head1, head2):
    newlist = LinkedList()
    node = head1
    while node is not None:
        newlist.add_to_list(node._element)
        node = node._next
    node = head2
    while node is not None:
        newlist.add_to_list(node._element)
        node = node._next
    return newlist


l1 = LinkedList()
l2 = LinkedList()

l1.add_to_list(1)
l1.add_to_list(2)
l1.add_to_list(3)
l2.add_to_list(4)
l2.add_to_list(5)
l2.add_to_list(6)
conlist = concatenate(l1.head(), l2.head())
conlist.print()
