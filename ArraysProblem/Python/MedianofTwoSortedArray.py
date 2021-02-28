lst1 = [1,3,5,6,7,8,9,11]
lst2 = [1,4,6,8,12,14,15,17]

s = len(lst1) + len(lst2)
print(s)

l = lst1 + lst2
l.sort()
print(l)
# print("Checking median " ,(l[7] +  l[8])/2)


def medianoftwosortedarrays(lst1,lst2):
    n , m = len(lst1) , len(lst2)
    i = j = 0
    finallist = []
    while i < n and j < m :
        if lst1[i] <= lst2[j] :
            finallist.append(lst1[i])
            i +=1
        else:
            finallist.append(lst2[j])
            j +=1

    while i < n :
        finallist.append(lst1[i])
        i +=1

    while j < m :
        finallist.append(lst2[j])
        j +=1
    median = 0
    if (n + m)%2 == 1:
        print("Median From Odd")
        median = finallist[(n+m)//2 + 1]
    else:
        print("Median From Even ")
        median = (finallist[(n+m)//2 -1] + finallist[(n + m)//2 + 1]) / 2

    print(median)

        




medianoftwosortedarrays(lst1,lst2)

