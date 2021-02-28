#
# def NumberOccuringOddNumberofTimes(A):
#
#     for i in A:
#         count = 0
#         for j in A:
#             if i == j:
#                 count +=1
#
#         if count %2 != 0:
#             return i


#
# def NumberOccuringOddNumberofTimes(A):
#
#     count_dict = dict()
#     elements = []
#     for i in A:
#         if i not in count_dict.keys():
#             count_dict[i] = 1
#         else:
#             count_dict[i] +=1
#
#     for key in count_dict.keys():
#         if count_dict[key] % 2 !=0:
#             elements.append(key)
#
#     if len(elements) == 0:
#         return -1
#     else:
#         return elements

def NumberOccuringOddNumberofTimes(A):
    """This is a Program which returns elements occuring oddd number of times
    in O(n) time and O(1) space
    """

    answer = 0
    for j in A:
        answer = answer ^ j
    return answer


print(NumberOccuringOddNumberofTimes([2,3,2,3,3]))