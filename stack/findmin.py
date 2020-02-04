class ArrayStack:

    def __init__(self):
        self._data = []
        self._min = []

    def is_empty(self):
        return len(self._data) == 0

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            pointer = self._data[-1]
            self._data.pop()
            if pointer == self._min[-1]:
                self._min.pop()

    def push(self, e):
        if not self.is_empty():
            if e < self._min[-1]:
                self._min.append(e)
        else:
            self._min.append(e)
        self._data.append(e)

    def min(self):
        return self._min[-1]


S = ArrayStack()
S.push(3)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())