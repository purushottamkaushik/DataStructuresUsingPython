



# def subsetwithgivensum(a,n,sum):
#
#     for i in range(n):
#         for j in range(i+1,n):
#             if a[i] + a[j] == sum:
#                 print("A[i] " ,a[i] ,"A[j]" ,a[j])
#                 return True
#
#
#     return False
#
# sorted_array = [9,10,11,15,26,36]


def subsetwithgivensum(a,n ,sum):
    l = 0
    r = 0
    for i in range(n-2):
        if a[i] > a[i+1]:
            break
    r = i
    l = (i+1) % n

    while l!=r :
        if (a[l] + a[r]) == sum :
            return True
        if (a[l] + a[r]) < sum:
            l = (l+1) % n
        else :
            r = (n+r-1) % n

    return False

sorted_rotated_array = [11,15,6,8,9,10]

print(subsetwithgivensum(sorted_rotated_array,len(sorted_rotated_array),20))