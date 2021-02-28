class Solution:
    def findDisappearedNumbers(self, nums):
        lst = []
        if not nums:
            return lst
        
        m = max(nums)
        
        for i in range(len(nums)):
            print(i)
            if i+1 in nums:
                continue
            else:
                lst.append(i+1)
        
        return lst        

        def findDisappearedNumbers2(self, nums):
            s = set(nums)
        
            n = len(nums) + 1
            lst = []
            for i in range(1,n):
                if i not in s:
                    lst.append(i)
                
            return lst    


s = Solution().findDisappearedNumbers([1,1])
print(s)