
#
# def LargestContigousSubArray(a,n):
#     """This accepts an array and its length as input
#     and returns the largestcontigous sum of index
#     """
#
#     max_sum = a[0]
#     max_curr = a[0]
#
#     for j in range(1,len(a)):
#         max_curr = max(max_curr , max_curr + a[j])
#
#         if max_sum <= max_curr:
#             max_sum = max_curr
#
#     return max_sum

def LargestContigousSubArray(a,l):
    max_sum = -100

    for i in range(l):
        sum = 0
        for j in range(i+1,l):
            sum +=a[j]

            if max_sum < sum :
                max_sum = sum

    return max_sum


if __name__=="__main__":
    l = [-2,-3,4,1,-2,1,5,-3]
    print(LargestContigousSubArray(l,len(l)))
