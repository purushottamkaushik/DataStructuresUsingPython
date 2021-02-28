class Solution1:
    def myPow(self, x,n):
        return x ** (n)

# Time limit Exceeded Solution
#
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#
#         if n < 0:
#             n = -n
#             x = 1 / x
#
#         val = 1
#         for j in range(1, n + 1):
#             val *= x
#         return val


class Solution:

    def fastPow(self, x, n):
        if n == 0:
            return 1.0
        A = self.fastPow(x, n / 2)

        if n % 2 == 0:
            return A * A
        else:
            return A * A * x

    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1 / x
            n = -n

        return self.fastPow(x, n)


s = Solution()
print(s.myPow(2,10))