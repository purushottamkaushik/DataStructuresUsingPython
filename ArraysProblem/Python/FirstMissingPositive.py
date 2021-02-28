# Level : HARD

# def firstmissingpositive(lst):
#     lst.sort()
#     print(lst)
#     # print(max(lst))
#     count = 0
#     for i in range(len(lst)-1):
#         count = i
#         if lst[i] < 0:
#             continue
#         elif lst[i] > 0 and lst[i] + 1 != lst[i+1]:
#             print(lst[i]+1)
#             break
#         else:
#             continue
#     print(count)        
#     if count == len(lst) - 2 :
#         print(lst[count]  +1 )        


def firstmissingpositive(arr):
    result  = 1
    arr.sort()
    print(arr)
    for i in range(len(arr)):
        if arr[i] == result :
            result +=1

    return result


print(firstmissingpositive([1,0,2]))