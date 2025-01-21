"""
Solution to LeetCode Problem 14: https://leetcode.com/problems/longest-common-prefix/
Authors: Bradley Dettmer, Jamie Palatnik
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string_len = min([len(x) for x in strs])

        prefix = ""

        for i in range(shortest_string_len):
            column_of_chars = [word[i] for word in strs]
            if len(set(column_of_chars)) == 1:
                prefix = prefix + column_of_chars[0]
            else: 
                return prefix

        return shortest_string_len

s = Solution()
assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert s.longestCommonPrefix(["dog","racecar","car"]) == ""