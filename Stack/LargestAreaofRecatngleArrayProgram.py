# Input: [2,1,5,6,2,3]
# Output: 10
# Level: Hard
# Problem Practice Link: https://leetcode.com/problems/largest-rectangle-in-histogram/


heights = [2,1,5,6,2,3]

# Approach 1

# def findleftIndex(arr,index):
# 	j = index - 1 
# 	while j >=0 and heights[j]>=heights[index]:
# 		j -=1
# 	return j
		

# def findRightIndex(arr,index):
# 	j = index + 1 
# 	while j < len(heights) and heights[j] >= heights[index]:
# 		j +=1
# 	return j



# def findMaxArea(heights):

# 	if len(heights) == 0:
# 		return 0
# 	maxArea = - 1
# 	for i in range(len(heights)):
# 		leftIndex = findleftIndex(heights,i)
# 		rightIndex = findRightIndex(heights , i)

# 		width = rightIndex - leftIndex - 1	

# 		currentArea = width * heights[i]
# 		if currentArea > maxArea:
# 			maxArea = currentArea

# 	return maxArea

# print(findMaxArea(heights))			







