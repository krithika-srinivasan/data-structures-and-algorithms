class ArrayQueue:
    DEFAULT_QUEUE_SIZE = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_QUEUE_SIZE  # The size of the queue
        self._size = 0  # Number of elements in the queue
        self._front = 0  # Head of the queue
        self._back = 0  # Tail of the queue

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._back]

    def dequeue_front(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._data[self._front]
        self._data[self._front] = None  # Help with garbage collection
        self._front = (self._front + 1) % len(self._data)  # Keep moving the head to the right until it wraps around
        self._size -= 1
        return head

    def dequeue_back(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        tail = self._data[self._back]
        self._data[self._back] = None  # Help with garbage collection
        self._back = (self._back - 1) % len(self._data)  # Keep moving the head to the right until it wraps around
        self._size -= 1
        return tail

    def enqueue_front(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        back = (self._front + self._size) % len(self._data)  # Insert it at the end of the sequence even if that means
        # wrapping around
        self._data[back] = e
        self._size += 1

    def enqueue_back(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        back = (self._size - self._back) % len(self._data)  # Insert it at the end of the sequence even if that means
        # wrapping around
        self._data[back] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]  # Reformat the queue so that the head is at index 0 again
            walk = (walk + 1) % len(old)
        self._front = 0


class Empty(Exception):
    pass
