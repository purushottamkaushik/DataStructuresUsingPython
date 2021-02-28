

def binarySearch(a,num):
    l = 0
    r = len(a) - 1
    print(r)
    while l <= r :
        mid = (l+r) // 2
        print("Mid is " , mid)
        if num == a[mid]:
            return mid
        elif num > a[mid]:
            l = mid + 1
        elif num < a[mid]:
            r = mid-1

    return False;

print(binarySearch([1,2,3,4,5,6,7],3))