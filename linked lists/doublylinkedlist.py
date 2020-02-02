class _DoublyLinkedList:
    class _Node:
        __slots__ = '_element', '_next', 'prev'

        def __init__(self, element, next, prev):
            self._prev = prev
            self._next = next
            self._element = element

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_between(self, e, before, after):
        newnode = self._Node(e, after, before)
        before._next = newnode
        after._prev = newnode
        self._size += 1

    def delete(self, node):
        after = node._next
        before = node._prev
        before._next = after
        after._prev = before
        val = node._element
        node._element = node._next = node._prev = 0
        return val
