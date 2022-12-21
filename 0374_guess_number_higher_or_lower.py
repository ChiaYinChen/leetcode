"""
0374. Guess Number Higher or Lower (Easy)
https://leetcode.com/problems/guess-number-higher-or-lower/
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            # "left + (right - left) // 2" is faster than "(left + right) // 2"
            # because the latter one could have integer overflow (becoming negative).
            # that could result infinite loop.
            mid = (left + right) // 2
            ans = guess(mid)
            if ans == 1:
                left = mid + 1
            elif ans == -1:
                right = mid - 1
            else:
                return mid
