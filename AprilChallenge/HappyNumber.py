# Problem Statement:
# Write an algorithm to determine if a number n is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
# Return True if n is a happy number, and False if not.
# Example: 
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# def getNextNumber(num):
#     sum = 0
#     while num > 0 :
#         rem = num % 10
#         sum +=rem**2
#         num = num //10

#     return sum


# def happyNumber(num):
# 	original = num
# 	numbers = set()
# 	loop = True
# 	while num != 1:
# 		n1 = getNextNumber(num)
# 		if n1 in  numbers:
# 			print(n1)
# 			print(numbers)
# 			print("Not a happy Number")
# 			break
# 		else:
# 			numbers.add(n1)
# 			num = n1 
# 	if num == 1 :
# 		print("Num {} Its a Happy number".format(original))

# happyNumber(116)


class Solution:

    def getNextNumber(self, num):

        sum = 0

        while num is not None and num > 0:
            rem = num % 10
            sum += rem ** 2
            num = num // 10
        return sum

    def isHappy(self, n):
        numbers = set()
        print(n)
        while n != 1 and n not in numbers:
            numbers.add(n)
            print("Printing n in loop " ,n)
            n = self.getNextNumber(n)

        print("N after the loop " ,n)

        return n == 1


print(Solution().isHappy(19))
