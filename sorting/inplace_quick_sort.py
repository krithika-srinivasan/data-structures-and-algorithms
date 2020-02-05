def inplace_quick_sort(S, start, end):
    if start > end:
        return

    pivot = S[end]
    left = start
    right = end - 1

    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1

    S[left], S[end] = S[end], S[left]

    inplace_quick_sort(S, start, left - 1)
    inplace_quick_sort(S, left+1, end)


S = [4, 2, 6, 8, 3, 9, 5, 11]
inplace_quick_sort(S, 0, 7)
print(S)