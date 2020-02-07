class LinkedList:
    class _Node:
        __slots__ = '_element', '_prev', '_next', '_repeat'

        def __init__(self, element, prev, next, repeat=False):
            self._element = element
            self._prev = prev
            self._next = next
            self._repeat = repeat

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._head = self._header
        self._size = 0
        self._values = []

    def add(self, e):
        newnode = self._Node(e, self._head, self._trailer)
        self._head._next = newnode
        self._trailer._prev = newnode
        self._head = newnode
        if len(self._values) == 0 or e not in self._values:
            self._values.append(e)
        else:
            newnode._repeat = True

    def remove_duplicates(self):
        walk = self._header._next
        while walk != self._trailer:
            if walk._repeat:
                node_delete = walk
                self._delete(node_delete)
            walk = walk._next

    def _delete(self, node):
        before = node._prev
        after = node._next
        node = None
        before._next = after
        after._prev = before

    def print(self):
        walk = self._header._next
        elements = []
        while walk != self._trailer:
            elements.append(walk._element)
            walk = walk._next
        print(elements)

ll = LinkedList()
ll.add(2)
ll.add(1)
ll.add(2)
ll.add(3)
ll.print()
ll.remove_duplicates()
ll.print()