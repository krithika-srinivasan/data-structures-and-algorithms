class QueueWithStacks():
    class _ArrayStack:

        def __init__(self):
            self._data = []

        def is_empty(self):
            return len(self._data) == 0

        def push(self, e):
            self._data.append(e)

        def pop(self):
            if len(self._data) == 0:
                raise Empty('Stack is empty')
            element = self._data[-1]
            self._data.pop()
            return element

        def peek(self):
            if len(self._data) == 0:
                raise Empty('Stack is empty')
            print(self._data[-1])

    def __init__(self):
        self._S1 = self._ArrayStack()
        self._S2 = self._ArrayStack()

    def enqueue(self, e):
        self._S1.push(e)

    def dequeue(self):
        if self._S2.is_empty():
            raise Empty('Queue is empty')
        self._transfer()
        self._S2.pop()

    def peek(self):
        if self._S2.is_empty() and self._S1.is_empty():
            raise Empty('Queue is empty')
        self._transfer()
        self._S2.peek()

    def _transfer(self):
        while not self._S1.is_empty():
            item = self._S1.pop()
            self._S2.push(item)


class Empty(Exception):
    pass

Q = QueueWithStacks()
Q.enqueue(2)
Q.enqueue(4)
Q.enqueue(7)
Q.enqueue(2)
Q.peek()
Q.dequeue()
Q.peek()
