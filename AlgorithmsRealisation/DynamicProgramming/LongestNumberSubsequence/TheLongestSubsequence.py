A = [1, 2, 5, 3, 6, 9, 2, 3, 5, 10, 7, 23, 1]
n = len(A)
D = [1] * n


def getLonggestSubsequence(A):
    for i in range(0, n):
        for j in range(0, i - 1):
            if A[j] < A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1


getLonggestSubsequence(A)
