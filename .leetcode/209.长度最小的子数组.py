#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1
        if n==0:
            return 0
        i, j = 0,0
        total = 0
        while j < n:
            total += nums[j]
            while total >= target:
                ans = min(ans, j-i+1)
                total -= nums[i]
                i += 1
            j += 1
        return 0 if ans==n+1 else ans

            
            
# @lc code=end

