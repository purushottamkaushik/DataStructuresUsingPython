
# def reverse(s):
#     s1 = ""
#     for i in s[::-1]:
#         s1+=i
#     return s1
#
# def LongestPalindromicSubsequence(string):
#
#     """This is a Bruteforce implementation of the problem"""
#
#     string = list(string)
#     maxlength = 0
#     # for i in range(len(string)):
#     #     print("".join(string[i:]))
#
#
#
#
#     for i in range(len(string)):
#         string = "".join(string[i:])
#         length = 0
#         if string == reverse(string):
#              length = len(string)
#              print(i , " " , length)
#         if maxlength < length:
#             maxlength = length
#
#     return maxlength


# if __name__=="__main__":
#     string = "vabcba"
#     print("String length is " , len(string))
#     print(LongestPalindromicSubsequence(string))


# Bruteforce approach Recursive Approach
# def longestPalindromicSubsequnce(s, i, j):
#     if i == j:
#         return 1
#     if s[i] == s[j] and i + 1 == j:
#         return 2
#     if s[i] == s[j]:
#         return longestPalindromicSubsequnce(s, i + 1, j - 1)
#
#     return max(longestPalindromicSubsequnce(s, i + 1, j), longestPalindromicSubsequnce(s, i, j - 1))
#
#
# if __name__ == '__main__':
#     s = 'AAIC'
#     n = len(s)
#     print(longestPalindromicSubsequnce(s, 0, n - 1))
#
#
# # Dynamic Programing Approach
#
# def longestPS(s):
#     n = len(s)
#     dp = [[0 for x in range(n)] for x in range(n)]
#
#     for i in range(n):
#         dp[i][i] = 1
#
#     for x in range(2, n + 1):
#         for i in range(n - x + 1):
#             j = i + x - 1
#             if s[i] == s[j] and x == 2:
#                 dp[i][j] = 2
#             elif s[i] == s[j]:
#                 dp[i][j] = dp[i + 1][j - 1] + 2
#             else:
#                 dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]);
#
#     return dp[0][n - 1]
#
#
# if __name__ == '__main__':
#     s = 'AAIC'
#     n = len(s)
#     print(longestPS(s))
