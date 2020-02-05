def merge_sort(S):
    n = len(S)
    if n < 2:
        return  # list is already sorted
    mid = n // 2
    S1 = S[0:mid]  # copy of first half
    S2 = S[mid:n]  # copy of second half
    merge_sort(S1)  # sort copy of first half
    merge_sort(S2)  # sort copy of second half
    merge(S1, S2, S)  # merge sorted halves back into S


def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1


S = [4, 2, 6, 8, 3, 9, 5, 11]
merge_sort(S)
print(S)
