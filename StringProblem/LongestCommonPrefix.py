# class Solution:
#     """
#     Word by word Comparison
#     """
#     def commonprefix(self, prefix, str):
#         """
#         Function to return the common prefix in the two strings
#         :param prefix: String
#         :param str:  String
#         :return:  String
#         """
#         n1 = len(prefix)
#         n2 = len(str)
#
#         i = j = 0
#
#         while i < n1 and j < n2:
#             if prefix[i] != str[j]:
#                 break
#             i += 1
#             j += 1
#         return prefix[:i]
#
#     def longestcommonprefix(self, strs):
#
#         if len(strs) < 1:
#             return ""
#         prefix = strs[0]
#         for i in range(len(strs)):
#             prefix = self.commonprefix(prefix, strs[i])
#         return prefix
#
#
# class Solution1:
#     """
#     Character by character comparison ..
#     """
#     def findminlength(self, str):
#         min_len = len(str[0])
#
#         for j in range(1, len(str)):
#             if min_len > len(str[j]):
#                 min_len = len(str[j])
#         return min_len
#
#     def longestCommonPrefix(self, strs):
#
#         if len(strs) < 1:
#             return ""
#
#         minlen = self.findminlength(strs)
#         result = ""
#         for i in range(minlen):
#             ch = strs[0][i]
#             for j in range(1, len(strs)):
#                 if strs[j][i] != strs[0][i]:
#                     return result
#             result += ch
#         return result
#


class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort()
        n1 = len(strs[0])
        n2 = len(strs[-1])
        result = ""
        end = min(n1, n2)
        i = 0
        while i < end:
            if strs[0][i] != strs[-1][i]:
                break
            result += strs[0][i]
            i += 1
        return result


LCP = Solution()
print(LCP.longestCommonPrefix(['appliedcourse', 'appliedai', 'appliegate', 'applied']))
