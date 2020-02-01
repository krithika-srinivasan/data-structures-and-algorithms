class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def pointer(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        top = self._head._element
        old = self._head
        self._head = self._head._next
        old = None
        return top


ll = LinkedStack()
ll.push(3)
ll.push(4)
print(ll.pop())
print(ll.pointer())
