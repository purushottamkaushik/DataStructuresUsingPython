# Given an array of strings, group anagrams together.
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

import collections


class Solution:
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[tuple(sorted(word))].append(word)

        return [v for k, v in anagrams.items()]


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))



# ###########


# import collections
#
#
# class Solution:
#     def groupAnagrams(self, strs):
#         anagrams = collections.defaultdict(list)
#
#         for word in strs:
#             count = [0] * 26
#             for c in word:
#                 count[ord(c) - ord('a')] += 1
#             anagrams[tuple(count)].append(word)
#         return anagrams.values()

