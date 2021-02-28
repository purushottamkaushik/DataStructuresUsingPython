# for i in range(len(str)):
#     for j in range(i+1,len(str)):
#         if str[i] == str[j]:
#             str[j] = " "

# print(str)


# def duplicateRemove(str):
#     unique = []
#     for i in str:
#         if i not in unique:
#             unique.append(i)
#     print(''.join(unique))
#
#     # mylist = list(sorted(unique))
#     # # print(mylist)
#     # string = ''.join(mylist)
#     # print(string)
#
#     return None

def duplicateRemove(str):
    ascii = [0] * 26

    for i in str:
        j = ord(i)
        index = j - 97
        ascii[index] += 1

    print(ascii)

    lst = []
    for j in range(len(ascii)):
        if ascii[j] != 0:
            index = j + 97
            element = chr(index)
            lst.append(element)
    print(lst)

    string = ''.join(sorted(lst))
    print(string)


str = "abcdab"

duplicateRemove(str.lower())
