

#
# def FindTwoMissingNumber(A):
#     """Problem Solving 5.13 Problem on Arrays"""
#     missing_number = []
#     for i in range(1,len(A)+1):
#         if i in A: # time complexity of this line
#             continue
#         else:
#             print(i)
#             missing_number.append(i)
#     return missing_number

def FindTwoMissingNumber(A):
    n = len(A)
    m = n + 2
    sum = (m * (m+1)) // 2

    arraysum = 0
    for i in A:
        arraysum+=i

    print("Array Sum " , arraysum)
    print("Sum is  " , sum)
    # print("Differenece is " , sum - arraysum)

    difference = sum - arraysum
    avg = (difference) // 2

    print("The average is " ,avg)
    avgsum = 0
    for i in range(n):
        if A[i] <= avg+1:
            avgsum +=A[i]

    sumofElementsLessthanAverage = 0
    for i in range(n):
        if A[i] < avg+1:
            sumofElementsLessthanAverage +=A[i]

    print("AverageSum is " ,avgsum)
    print("SumOfElementsLessThanAverage " , sumofElementsLessthanAverage)
    firstNumber = avgsum - sumofElementsLessthanAverage
    secondNumber = difference -firstNumber

    print(firstNumber,secondNumber)

print(FindTwoMissingNumber([1,3,5,6]))
