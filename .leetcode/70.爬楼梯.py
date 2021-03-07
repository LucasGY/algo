#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2

        f1 = 1
        f2 = 2
        res = 0
        for i in range(3, n+1):
            res = f2 + f1
            f1 = f2
            f2 = res
        return res
# @lc code=end

