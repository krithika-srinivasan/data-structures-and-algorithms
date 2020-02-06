def is_permutation(s1, s2):
    sum1 = 0
    sum2 = 0
    for c1 in s1:
        sum1 = sum1 + ord(c1)
    for c2 in s2:
        sum2 = sum2 + ord(c2)
    return sum1 == sum2


a1 = 'abcd'
a2 = 'dabc'
a3 = 'pqrs'
print(is_permutation(a1,a2))
print(is_permutation(a1,a3))