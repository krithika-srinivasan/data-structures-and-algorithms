import ctypes  # Low level arrays

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):  # Get item at index k
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):  # Add object to array's end
        if self._n == self._capacity:  # If the array is full
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('Value not found')

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def print_array(self):
        for k in range(self._n):
            print(self._A[k])


arr = DynamicArray()

arr.append(3)
arr.append(5)
arr.append(4)
arr.append(6)
arr.print_array()
arr.remove(6)
arr.print_array()
