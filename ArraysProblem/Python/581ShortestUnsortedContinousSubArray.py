


def shortestUnsorted(nums) :
    copied = nums.copy()

    copied = sorted(copied)
    print(nums)
    print(copied)
    count = 1
    for j in range(len(nums)):
        if nums[j] != copied[j]:
            count +=1
    return count
nums = [2,6,4,8,10,9,15]
print(shortestUnsorted(nums))


# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         start, end = 0, len(nums)
#         snums = nums[:]
#         snums.sort()
#
#         for j in range(len(nums)):
#             if snums[j] != nums[j]:
#                 start = max(start, j)
#                 end = min(end, j)
#
#         if start - end >= 0:
#             return start - end + 1
#         else:
#             return 0
