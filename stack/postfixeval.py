from array_as_stack import ArrayStack


def postfixeval(expr):
    S = ArrayStack()
    operator = '+-/*'
    for c in expr:
        if c not in operator:
            S.push(c)
        if c in operator:
            if S.stacklen() < 2:
                raise ValueError('Not enough numbers')
            a = S.pop()
            b = S.pop()
            if c == '+':
                z = int(a) + int(b)
            if c == '-':
                z = int(a) - int(b)
            if c == '*':
                z = int(a) * int(b)
            if c == '/':
                z = int(a) / int(b)
            S.push(z)
    if S.stacklen() == 1:
        return S.pointer()
    else:
        print(S.pointer())

print(postfixeval('12+24++'))
