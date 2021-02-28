

# def replaceelementwithgreatest(arr):
#     output = []
#     for i in range(len(arr)-1):
#         max = arr[i+1]
#         for j in range(i+1 , len(arr)):
#             if max < arr[j]:
#                 max = arr[j]
#         output.append(max)
#     output.append(-1)
#     return output
    # print(output)

# def replaceelementwithgreatest(arr):
#     output = []
#     for i in range(len(arr) -1) :
#         element = max(arr[i+1:])
#         output.append(element)
#     output.append(-1)
#     print(output)
#     return output

"""Problem Statement:

Given an array arr, replace every element in that array with the greatest element among the elements to its right,
 and replace the last element with -1.
After doing so, return the array.
Example 1:
Input: arr = [17,18,5,4,6,1]    Output: [18,6,6,6,1,-1]
Constraints:
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
Level: Easy
"""



def replaceelementwithgreatest(arr) :
    n = len(arr)
    arr[n-1] = -1
    maxelement = arr[n -1 ]

    for i in range(n-2,-1,-1):
        #print("printing i " ,i)
        temp = arr[i]
        arr[i] = maxelement
        if temp>maxelement:
            maxelement = temp;
    print(arr)

arr = [17,18,5,4,6,1]
replaceelementwithgreatest(arr)

