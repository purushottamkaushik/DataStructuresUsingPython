class Solution:
    def frequencySort(self, s: str) -> str:

        d = dict()
        for i in s:
            d[i] = d.get(i, 0) +1
        result = ""
        for val in  sorted(d.items(),key= lambda x: x[1], reverse=True)  :
            result +=val[0] * val[1]
        return result


print(Solution().frequencySort("tree"))