from array_as_stack import ArrayStack

def match(expr):
    S = ArrayStack()
    left = '([{<'
    right = ')]}>'
    for c in expr:
        if c in left:
            S.push(c)
        elif c in right:
            if S.is_empty() == False:
                S.pop()
        else:
            pass
    if S.is_empty():
        return True
    else:
        return False

print(match('(Muffy) and (Unnibi)'))
print(match('(Muffy and (Unnibi)'))