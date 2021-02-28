# Problem Statement 

# We have to swap find the minimum swaps to balance a paranthesis
# [] ][][  ---- 2 
# [][][] ----- 0 
#[[[]]]][ ------ 1 


# 1 . [] ---- 0 
# 2 ][   ---- 1
# 3 [[]] ---- 0 
# 4 [] [ ] ---- 0 
# 5 ][][   -----2 
# 6 ]][[   -----3 


def minimumswaps(str):
	leftcount = 0
	rightcount = 0
	swaps = 0
	imbalance = 0 

	for j in list(str):
		if j == '[':
			leftcount +=1
			if imbalance > 0 :
				swaps = swaps + imbalance
				imbalance -=1

		if j ==']':
			rightcount +=1
			imbalance = rightcount - leftcount		 

	return swaps

print(minimumswaps("][[]"))


