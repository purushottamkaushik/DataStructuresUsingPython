
def PathNumbers(rows,cols):

	n = [ [ 0 for _ in range(cols) ] for _ in range(rows) ]
	print(n)

	for col in range(len(n[0])):
		n[0][col] = 1

	for row in range(len(n)):
		n[row][0] = 1	

	print("After Adjustment ")	
	print(n)	

	for row in range(1,len(n)):
		for col in range(1,len(n[row])):
			n[row][col] = n[row-1][col-1] + n[row-1][col] + n[row][col-1]

	print("After Filling the whole Matrix")
	
	for row in range(len(n)):
		print(n[row])	
	print("Number of Paths : " , n[-1][-1])	

PathNumbers(6,5)