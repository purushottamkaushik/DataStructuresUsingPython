# class Solution:
#     def reorganizeString(self, S: str) -> str:
#         n = len(S)
#         a = []
#         for count, c in sorted((S.count(c), c) for c in set(S)):
#             if count > (n + 1) / 2:
#                 return ""
#             a.extend(count * c)
#         result = [None] * n
#         # print(a)
#         result[::2] = a[n // 2:]
#         result[1::2] = a[:n // 2]
#         # print(result)
#         return "".join(result)
#
# s = Solution().reorganizeString("aab")
# print(s)
