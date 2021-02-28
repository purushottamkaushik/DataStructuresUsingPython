#def singleNumber(nums):
#	return (3 * (sum(set(nums))) - sum(nums)) // 2


def singleNumber(nums):
	mydict = dict()
	for num in nums:
		if num not in mydict.keys():
			mydict[num] = 1
		else :
			mydict[num] = mydict.get(num) + 1
	print(mydict)

	return [k for k,v in mydict.items() if v==1][0]


nums = [1,0,1,0,1,0,99]
print(singleNumber(nums))
