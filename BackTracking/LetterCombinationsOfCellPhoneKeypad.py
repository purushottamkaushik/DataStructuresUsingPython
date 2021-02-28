class Solution:
    def letterCombinations(self, digits):
        phone = {
                '2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z'],
                }
        result = []
        def recursive(combination,digits):
            print("Length of digits :{}   and digits {} ".format(len(digits),digits)) 
            print("Combination is : ", combination )
            if len(digits) == 0: 
                result.append(combination)
            else:
                for char in phone[digits[0]]:
                    recursive(combination+char , digits[1:])
    
        result = []
        if len(digits):
            recursive("",digits)
        
        return result

print(Solution().letterCombinations("23"))        