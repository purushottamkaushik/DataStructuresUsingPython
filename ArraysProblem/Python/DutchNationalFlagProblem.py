def DNF(a):
    c0 = 0
    c1 = 0
    c2 = 0
    for i in range(len(a)):
        if a[i] == 0:
            c0 += 1
        if a[i] == 1:
            c1 += 1
        if a[i] == 2:
            c2 += 1

    print(c0)
    print(c1)
    print(c2)

    sorted_list = []

    for i in range(c0):
        sorted_list.append(0)
    for i in range(c1):
        sorted_list.append(1)
    for i in range(c2):
        sorted_list.append(2)

    return sorted_list


#
# def insertionSort(a):
#     for j in range(1,len(a)):
#         key = a[j]
#         i = j -1
#         while i>=0 and a[i] > key:
#             a[i+1] = a[i]
#             i -=1
#
#         a[i+1] = key
#
#     return a


# print(DNF([0,1,0,1,2,1,2,1]))
# a = insertionSort([0,1,0,1,2,1,2,1])
# print(a)

def ducthSinglePass(a):
    """Dutch Flag Single Pass """
    l = c = 0
    h = len(a) - 1
    while c < h:
        if a[c] == 0:
            a[c], a[l] = a[l], a[c]
            c += 1
            l += 1
        if a[c] == 1:
            c +=1
        else:
            a[h] , a[c] = a[c] , a[h]
            h -=1

    return a

print(ducthSinglePass([0,1,0,1,2,1,2,1]))