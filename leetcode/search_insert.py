"""
Solution to Leetcode Problem 35: https://leetcode.com/problems/search-insert-position/description/
Authors: Samantha Tetef, Satyajit Sarangdhar, Ramapriya Radhakrishnan
"""


def searchInsert(self, nums: List[int], target: int) -> int:
    if len(nums) < 2:
        return int(target > nums[0])
    mid = len(nums) // 2
    if target < nums[mid]:
        return self.searchInsert(nums[0:mid], target)
    elif target == nums[mid]:
        return mid
    else:
        return mid + self.searchInsert(nums[mid:], target)
