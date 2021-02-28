# A row is considered as weak if it contains less soldiers than civilians
# 1 ---- Soldier 
# 2 ---- Civilian

mat = [
		[1,1,0,0,0],
		[1,1,1,1,0],
		[1,0,0,0,0],
		[1,1,0,0,0],
		[1,1,1,1,1]
	]

def kweakestrows(mat,k):
	c = 0
	d = dict()
	for i in range(len(mat)):
		count = 0
		for j in range(len(mat[i])):
			c +=1
			if mat[i][j] == 1:
				count +=1
			else:
				break	
		d[i] = count
	
	d = { k:v for k , v in sorted(d.items() , key=lambda x : x[1])}
 
	lst = []
	print("Printing c " , c )
	count = 0
	for key in d.keys():
		if count < k:
			lst.append(key)
			count +=1
	return lst		 		

mat = [[1,0,0,0],

 [1,1,1,1],

 [1,0,0,0],

 [1,0,0,0]
 ]


print(kweakestrows(mat,2)	)	 		
				
