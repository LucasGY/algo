#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                self.swap(nums, i, ptr)
                ptr += 1
        for i in range(ptr, len(nums)):
            if nums[i] == 1:
                self.swap(nums, i, ptr)
                ptr += 1

    def swap(self, array, i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

# @lc code=end

