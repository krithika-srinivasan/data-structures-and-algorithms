def insertion_sort(A):
    for k in range(0, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur


S = [4, 2, 6, 8, 3, 9, 5, 11]
insertion_sort(S)
print(S)