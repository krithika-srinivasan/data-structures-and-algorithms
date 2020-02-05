def quick_sort(S):
    n = len(S)
    if n < 2:
        return n
    pivot = S[0]
    L = []
    E = []
    G = []

    for i in range(0, n):
        if S[i] < pivot:
            L.append(S[i])
        elif pivot < S[i]:
            G.append(S[i])
        else:
            E.append(S[i])

    quick_sort(L)
    quick_sort(G)

    S = L + E + G
    print(S)


S = [4, 2, 6, 8, 3, 9, 5, 11]
quick_sort(S)