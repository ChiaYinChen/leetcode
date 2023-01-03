"""
0198. House Robber (Medium)
https://leetcode.com/problems/house-robber/
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        _size = len(nums)
        if _size == 1:
            return nums[0]
        elif _size == 2:
            return max(nums[0], nums[1])

        dp = [0 for _ in range(_size)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, _size):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]


def main():
    s = Solution()
    nums = [1, 2, 3, 1]
    print(f"Input: {nums} \nOutput: {s.rob(nums)}")
    nums = [2, 7, 9, 3, 1]
    print(f"Input: {nums} \nOutput: {s.rob(nums)}")


if __name__ == "__main__":
    main()
