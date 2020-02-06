def is_unique(s):
    if len(s) > 128:
        return False

    fl = [None] * 1000
    for c in s:
        ind = ord(c)
        if fl[ind]:
            return False
        fl[ind] = True
    return True


a = 'abcd'
b = 'abbd'
print(is_unique(a))
print(is_unique(b))