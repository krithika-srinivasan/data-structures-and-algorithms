class Cursor:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._cursor = self._header

    def left(self):
        if self._cursor == self._header:
            print('Already to the left')
        else:
            self._cursor = self._cursor._prev
            print('Shifted one char to the left')
        self.print()

    def right(self):
        if self._cursor == self._trailer:
            print('Already to the right')
        else:
            self._cursor = self._cursor._next
            print('Shifted one char to the right')
        self.print()

    def insert(self, c):
        newnode = self._Node(c, self._cursor, None)
        next = self._cursor._next
        next._prev = newnode
        newnode._next = next
        self._cursor._next = newnode
        self._cursor = newnode
        self.print()

    def delete(self):
        if self._cursor == self._trailer:
            print('Nothing to delete')
        else:
            self._cursor = self._cursor._prev
            self._cursor._next = None
        self.print()

    def print(self):
        node = self._header._next
        elements = []
        while node != self._trailer:
            elements.append(node._element)
            node = node._next
        str = "".join(elements)
        print(str)

c = Cursor()
c.insert('m')
c.insert('u')
c.insert('f')
c.insert('f')
c.insert('y')
c.left()
c.insert('f')
