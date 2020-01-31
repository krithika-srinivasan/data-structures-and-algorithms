class ArrayQueue:
    DEFAULT_QUEUE_SIZE = 10
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_QUEUE_SIZE
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return head

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0


class Empty(Exception):
    pass
