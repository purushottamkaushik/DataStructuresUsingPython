# def removeDuplicateAdjacentCharacters(s):
#
#
#     lst = [char for char in s]
#     n = len(s)
#     for i in range(1,n):
#         if lst[i] == lst[i-1]:
#             return removeDuplicateAdjacentCharacters(s[0:i-1] + s[i+1:n])

#
# def removeAdj(string):
#     string = list(string)
#     s = 0
#     prev = None
#     str_value = ""
#     for f in range(0, len(string)):
#         if (prev != string[f]):
#             string[s] = string[f]
#             s += 1
#         prev = string[f]
#     for i in range(s):
#         str_value += string[i]
#     return str_value


def removeAdj(string):
    string = list(string)
    s = 0
    prev = None

    for f in range(len(string)):
        if s == 0 or string[s - 1] != string[f]:
            string[s] = string[f];
            s += 1
            prev = string[f]
        else:
            s -= 1

    return "".join(string[0:s])


if __name__ == '__main__':
    string = "AABAABCCC"
    # string = "abbaca"
    print((removeAdj(string)))

# if __name__=="__main__":
#     s = "abbaca"
#     print(removeDuplicateAdjacentCharacters(s))
