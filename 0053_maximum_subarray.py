"""
0053. Maximum Subarray (Medium)
https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = 0
        max_ans = nums[0]
        for num in nums:
            ans = max(ans + num, num)
            max_ans = max(max_ans, ans)
        return max_ans


def main():
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: {nums} \nOutput: {s.maxSubArray(nums)}")
    nums = [1]
    print(f"Input: {nums} \nOutput: {s.maxSubArray(nums)}")
    nums = [5, 4, -1, 7, 8]
    print(f"Input: {nums} \nOutput: {s.maxSubArray(nums)}")


if __name__ == "__main__":
    main()
