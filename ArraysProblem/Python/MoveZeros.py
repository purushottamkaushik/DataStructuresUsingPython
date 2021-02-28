# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:
# Input:  [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

arr = [0,1,0,3,12]

# In this solution the order is not preserved
# def movezeros(arr):

#     j = len(arr) - 1
#     print(arr)
#     # print(j)
#     for i in range(len(arr)):
#         if i == j:
#             break
#         if arr[i] == 0 and arr[j] != 0 and j >i:
#             # print(i,j )
#             arr[i] , arr[j] = arr[j] , arr[i]
#             # print(arr)
#             j -=1
#    return arr


# it uses an extra space...

# def movezeros(nums):
#     """
#     Time complexity ---- O(n)
#     Space Complexity ----- O(n)
#     """
#     result = []

#     for num in nums:
#         if num != 0 :
#             result.append(num)

#     for num in nums:
#         if num == 0:
#             result.append(num)

#     return result                 


# def  movezeros(nums):

#     countzeros = 0
#     for num in nums:
#         if num == 0 :
#             countzeros +=1
#             nums.remove(num)
            

#     for i in range(countzeros):
#         nums.append(0)

#     return nums 


def movezeros(nums):
    slow = 0 

    for fast in range(len(nums)):
        if nums[fast] != 0 :
            nums[slow] , nums[fast] = nums[fast] , nums[slow]
            slow +=1 
    return nums                 
print(movezeros(arr))

