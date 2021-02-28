# def runLengthEncoding(s):
#     """This is a simple for loop and solution which runs in order of O(n) time complexity """
#     i=0
#     while i < len(s)-1:
#         count =1
#         while i <len(s) -1 and s[i] == s[i+1]:
#             i +=1
#             count +=1
#
#         print(s[i],count,sep="",end="")
#         i +=1

# def runLengthEncoding(s):
#
#     mydict = {}
#     for i in s:
#         # print(i)
#         mydict[i] = mydict.get(i,0) +1
#
#     lst =[]
#     for k,v in mydict.items():
#         lst.append(str(k))
#         lst.append(str(v))
#
#     s1 = ''.join(lst)
#     print(s1)


s = "aaaabbcccccdefff"
runLengthEncoding(s)
