class LinkedList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._head = self._header

    def add_node(self, e):
        newnode = self._Node(e, None)
        self._head._next = newnode
        self._head = newnode

    def elements(self):
        walk = self._header._next
        elements = []
        while walk is not None:
            elements.append(walk._element)
            walk = walk._next
        return elements

    def print(self):
        walk = self._header._next
        elements = []
        while walk is not None:
            elements.append(walk._element)
            walk = walk._next
        print(elements)


def numberify(elements):
    number = 0
    for i in range(0, len(elements)):
        number = number + (elements[i] * (10 ** i))
    return number


def denumberify(number, digits=[]):
    if number == 0:
        return digits
    digits.append(number % 10)
    number = number // 10
    return denumberify(number, digits)


def add_linked_lists(l1, l2):
    number1 = numberify(l1.elements())
    number2 = numberify(l2.elements())
    number_sum = number1 + number2
    numbers_new = denumberify(number_sum)
    l3 = LinkedList()
    for i in range(0, len(numbers_new)):
        l3.add_node(numbers_new[i])
    l3.print()

l1 = LinkedList()
l1.add_node(7)
l1.add_node(1)
l1.add_node(6)
l1.print()
l2 = LinkedList()
l2.add_node(5)
l2.add_node(9)
l2.add_node(2)
l2.print()
add_linked_lists(l1, l2)