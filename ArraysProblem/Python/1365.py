# def smallerthancurrentElement(nums):
#     mydict = dict()
#     for i ,v in enumerate(sorted(nums)):
#         if v not in mydict.keys():
#             mydict[v] = i
#
#     result = [mydict[value] for value in nums]
#     return result

def smallerthancurrentElement(num) :
    count = [0] * 100
    # print(len(count))

    for i in num:
        count[i] = count[i]+1
    # print(count)

    #prefix sum
    for i in range(1,100):
        count[i] = count[i] + count[i-1]
    # print(count)

    #traverse
    result = [0] * len(num)

    for i ,val in enumerate(num) :
        if val >0 :
            result[i] = count[val-1]
    # print(result)
    return result

num = [8,1,2,2,3 ]

smallerthancurrentElement(num)