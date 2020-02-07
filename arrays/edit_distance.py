def edit_distance_one(s1, s2):
    stack = []
    for c in s1:
        stack.append(c)
    discrepancy = True
    rev = s2[::-1]
    for c in rev:
        print(stack)
        print('Letter in consideration: {}'.format(c))
        if c != stack[-1] and discrepancy:
            discrepancy = False
            print('Pop {}'.format(stack[-1]))
            stack.pop()

        elif c != stack[-1] and not discrepancy:
            return False

        else:
            print('Pop {}'.format(stack[-1]))
            stack.pop()

    if len(stack) == 0:
        return True


a = 'abcd'
b = 'abbb'
print(edit_distance_one(a, b))
