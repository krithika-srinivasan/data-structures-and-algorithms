class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def head(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def tail(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._tail._element

    def enqueue(self, e):
        newnode = self._Node(e, None)
        if self.is_empty():
            self._head = newnode
        else:
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        head = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return head


class Empty(Exception):
    pass


ql = LinkedQueue()
ql.enqueue(2)
ql.enqueue(3)
print(ql.head())
print(ql.tail())
print(ql.dequeue())
