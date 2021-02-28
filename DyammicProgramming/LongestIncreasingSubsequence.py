# lst = [2,4,6,3,5,7,9]
lst = [1]
# brute Force Approach....

# def longestIncreasingSubsequence(a):
# 	lis = [a[0]]
# 	highest = a[0]
# 	l = 1 
# 	for i in range(1,len(a)):
# 		if a[i] >= highest :
# 			highest = a[i]
# 			l +=1
# 	print(l)	


# Using Dynammic Programming .
def longestIncreasingSubsequence(a):

	highest = 0 
	l = []
	l.append(a[0])
	for i in range(1,len(a)):
		if a[i] > highest:
			l.append(a[i])
			highest = a[i]
	print(l)
	print(len(l))		


longestIncreasingSubsequence(lst)		  