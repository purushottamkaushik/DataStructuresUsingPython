# Problem Statement:
# Given a collection of distinct integers, return all possible permutations.
# Input: [1,2,3]
# Output:[  [1,2,3], [1,3,2],  [2,1,3],  [2,3,1],  [3,1,2],  [3,2,1]]
result = []

nums = [1,2,3]
def Permutations(nums,l ,r):

	if l == r-1:
		result.append(nums[:])
	else:
		for i in range(l,r):
			nums[l] , nums[i] = nums[i] , nums[l]
			Permutations(nums,l+1,r)
			nums[l] , nums[i] = nums[i] , nums[l]



def permutate(nums):
	n = len(nums)
	Permutations(nums,0,n)
	print(result)

permutate([1,2,3])
