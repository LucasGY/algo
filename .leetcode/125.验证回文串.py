#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        else:
            reverse_str = ''.join(item.lower() for item in s if item.isalnum())
        return reverse_str == reverse_str[::-1]
# @lc code=end

