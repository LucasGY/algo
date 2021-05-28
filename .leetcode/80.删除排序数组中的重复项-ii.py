# @before-stub-for-debug-begin
from python3problem80 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[j]==nums[i]:
                if count==1:
                    j += 1
                    nums[j] = nums[i]
                    count += 1
                else:
                    pass
            else:
                count = 1
                j += 1
                nums[j] = nums[i]
        return j+1

                
                

                
            
            
# @lc code=end

