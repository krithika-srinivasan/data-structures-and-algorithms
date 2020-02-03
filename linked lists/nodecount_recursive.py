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

    def head(self):
        return self._head

    def add_to_list(self, e):
        newnode = self._Node(e, None)
        if self.is_empty():
            self._head = newnode
        else:
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1

def listlen(node, count=0):
    if node is None:
        return count
    else:
        count = 1 + listlen(node._next, count)

    return count

l = LinkedList()
l.add_to_list(1)
l.add_to_list(2)
l.add_to_list(3)
l.print()
print(listlen(l.head()))