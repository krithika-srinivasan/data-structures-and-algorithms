def move(a, b):
    print('Move from {} to {}'.format(a, b))


def hanoi(num_discs, first, second, third):
    if num_discs == 0:
        pass
    else:
        hanoi(num_discs - 1, first, third, second)
        move(first, third)
        hanoi(num_discs - 1, second, first, third)


hanoi(3, 'A', 'B', 'C')
