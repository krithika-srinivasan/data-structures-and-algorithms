class BinaryTree:

    class _Node:
        __slots__ = '_element', '_parent', '_left_child', '_right_child'
        def __init__(self, element, parent, left_child, right_child):
            self._element = element
            self._parent = parent
            self._left_child = left_child
            self._right_child = right_child

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def parent(self, node):
        return node._parent

    def left(self, node):
        return node._left_child

    def right(self, node):
        return node._right_child

    def sibling(self, node):
        parent = node._parent
        if parent is None:
            return None
        else:
            if node == parent._left:
                return parent._right
            else:
                return parent._left

    def children(self, node):
        if self.left(node) is not None:
            yield self.left(node)
        if self.right(node) is not None:
            yield self.right(node)

    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root already exists')
        self._size += 1
        self._root = self._Node(e, None, None, None)

    def add_left(self, node, e):
        if node._left is not None:
            raise ValueError('Node already has a left child')
        self._size += 1
        node._left = self._Node(e, node, None, None)

    def add_right(self, node, e):
        if node._right is not None:
            raise ValueError('Node already has a right child')
        self._size += 1
        node._right = self._Node(e, node, None, None)

# bt = BinaryTree()
# bt.add_root(3)
# bt.add_left(root, 2)
test = [1,2,3,4,5]
print(min(test))