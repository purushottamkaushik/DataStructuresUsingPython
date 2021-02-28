class Solution:

    def decode(self, index, s):
        if index == len(s):
            return 1
        if s[index] == '0':
            return 0
        if index == len(s) - 1:
            return 1
        return self.decode(index + 1, s) + self.decode(index + 2, s) if ((int)(s[index: index + 2])) <= 26 else 0

    def numDecodings(self, s: str) -> int:

        if not s:
            return 0
        else:
            return self.decode(0, s)
