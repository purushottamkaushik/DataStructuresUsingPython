
def targetreturn(A ,index):

    lst = []
    for i in range(len(A)):
        lst.insert(index[i],A[i])
    print(lst)

    return lst

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
targetreturn(nums,index)
