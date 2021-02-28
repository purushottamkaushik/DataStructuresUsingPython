#
# def firstNonRepeatingCharacter (s):
#     """ THis is O(n2) time and O(1) space implementation """
#     s = list(s)
#     for i in range(len(s)):
#         char = s[i];
#         count = 1
#         for j in range(i+1,len(s)):
#             if s[i] == s[j]:
#                 count +=1
#
#         if count == 1 :
#             print(s[i])
#             break


# def firstNonRepeatingCharacter(s):
#     """
#     This is O(n) time complexity and O(n) using hashtable as a data structure
#     """
#     s = list(s)
#     mydict = {}
#
#     for j in s:
#         mydict[j] = mydict.get(j,0) + 1
#
#     # print(mydict)
#
#     for k,v in mydict.items():
#         if v == 1 :
#             print(k)
#             break


# def firstNonRepeatingCharacter(s):
#     """
#     It is the implementation which only uses one scan to build the solution
#     :param s:
#     :return:
#     """
#
#     s = list(s)
#
#     mydict = {}
#     myindexdict = {}
#     for j in range(len(s)):
#         mydict[s[j]] = mydict.get(s[j],0) + 1
#         if s[j] not in myindexdict.keys():
#             myindexdict[s[j]] = j
#
#
#     print(mydict)
#     print(myindexdict)

if __name__ == "__main__":
    string = "abcdab"
    firstNonRepeatingCharacter(string)
