def palindrome_permutation(s):
    if s == s[::-1]:
        return True

    nospace = []
    for c in s:
        if c != ' ':
            nospace.append(c)

    nospace.sort()
    stack = []
    for c in nospace:
        if len(stack) == 0:
            stack.append(c)
        elif c != stack[-1]:
            stack.append(c)
        else:
            stack.pop()

    if len(nospace) % 2 == 0 and len(stack) == 0:
        return True
    elif len(nospace) % 2 != 0 and len(stack) == 1:
        return True
    else:
        return False


s = 'tact coa'
print(palindrome_permutation(s))