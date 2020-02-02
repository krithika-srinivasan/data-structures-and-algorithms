class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def head(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._tail._next._element

    def tail(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._tail._element

    def enqueue(self, e):
        newnode = self._Node(e, None)
        if self.is_empty():
            newnode._next = newnode
        else:
            newnode._next = self._tail._next
            self._tail._next = newnode

        self._tail = newnode
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        oldhead = self._tail._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        else:
            self._tail._next = oldhead._next
        return oldhead._element


class Empty(Exception):
    pass


cl = CircularQueue()
cl.enqueue(2)
cl.enqueue(3)
print(cl.head())
print(cl.dequeue())