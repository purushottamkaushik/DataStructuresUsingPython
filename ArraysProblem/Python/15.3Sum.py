

#
# def threesum(arr):
#
#     outer = list()
#     for i in range(len(arr)-2) :
#         for j in range(i+1,len(arr)-1):
#
#             for k in range(j+1,len(arr)):
#                 triplet = []
#                 if (arr[i] + arr[j] + arr[k]) == 0 :
#                     triplet.append(arr[i])
#                     triplet.append(arr[j])
#                     triplet.append(arr[k])
#                 if len(triplet) == 3 :
#                     outer.insert(0, triplet)





def threesum(nums) :

    n = len(nums)
    nums.sort()
    result = []
    for i in range(n-1):
        l = i +1
        r = n-1

        while l <r :
            current_sum = nums[i] + nums[l] + nums[r]
            if current_sum == 0:
                result.append([nums[i],nums[l],nums[r]])
                l +=1
                r -=1
            elif current_sum < 0:
                l +=1
            else:
                r -=1
    print("result is " , result)
    return  set(list(tuple(x) for x in result))

nums = [-1,0,1,2,-1,-4]

print(threesum(nums))