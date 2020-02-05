class Heap:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[j], self._data[i] = self._data[i], self._data[j]

    def _heapup(self, j):
        parent = self._parent(j)
        while j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._heapup(parent)

    def _heapdown(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] > self._data[j]:
                self._swap(small_child, j)
                self._heapdown(small_child)

    def add(self, e):
        self._data.append(e)
        self._heapup(len(self._data) - 1)

    def min(self):
        if len(self._data) == 0:
            raise Empty('Heap is empty')
        return self._data[0]

    def remove_min(self):
        if len(self._data) == 0:
            raise Empty('Heap is empty')
        self._swap(0, len(self._data) - 1)
        self._data.pop()
        self._heapdown(0)

    def print(self):
        print(self._data)


class Empty(Exception):
    pass

hp = Heap()
hp.add(5)
hp.add(1)
hp.add(3)
hp.add(2)
hp.print()