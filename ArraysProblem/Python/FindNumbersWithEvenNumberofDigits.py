nums = [12,345,2,6,7869]

# def evennumofdigits(nums):
#     count = 0

#     for i in range(len(nums)):
#         l = len(str(nums[i]))
#         if l %2==0:
#             count +=1

#     return count

def evennumofdigits(nums):
    print("FROM this function")
    return sum([1 for val in nums if len(str(val))%2==0])


ans = evennumofdigits(nums)                
print("Number of digits with even number of digits are " , ans)

