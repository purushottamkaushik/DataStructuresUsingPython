# copied ...
a = [2,3,4,5]

def subsetsum(a,sum):
	lst = [[ -1 for j in range(len(a))] for _ in range(sum)]
	
	for i in range(sum):
		if sum == a[0]:
			lst[i][0] = 1
		else:
			lst[i][0] = 0	

	for i in range(1,sum+1):
		for j in range(1,len(a) + 1):
			lst[i][j] = lst[i][j-1]

			if i <= a[j]: # i is nothing but sum 
				lst[i][j] = lst[i][j] or lst[i - a[i]][ j]





	for i in range(len(lst)):
		print(lst[i])		

subsetsum(a,10)
