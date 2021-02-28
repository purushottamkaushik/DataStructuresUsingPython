def MergeSort(a, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(a, p, q)
        MergeSort(a, q + 1, r)
        Merge(a, p, q, r)


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + j + 1]

    k = p
    i = 0
    j = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            k += 1
        else:
            A[k] = R[j]
            j += 1
            k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


a = [2, 1, 3, 5, 4]
for i in a:
    print(i)
MergeSort(a, 0, len(a) - 1)

print("After Sorting")

for i in a:
    print(i)
