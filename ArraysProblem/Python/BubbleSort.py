

def bubbleSort(a):

    n = len(a)
    for i in range(n):
        for j in range( n-1-i):
            if (a[j] > a[j+1]):
                a[j] , a[j+1] = a[j+1] , a[j]



a = [1,3,2,4,6,5]
print("Before sorting " ,a)
bubbleSort(a)
print("After sorting " ,a )
