"""
0213. House Robber II (Medium)
https://leetcode.com/problems/house-robber-ii/
"""


class Solution:
    """
    https://leetcode.com/problems/house-robber-ii/solutions/893957/python-just-use-house-robber-twice/

    Now, what we have here is circular pattern. Imagine, that we have 10 houses: a0, a1, a2, a3, ... a9
    Then we have two possible options:

    1. Rob house `a0`, then we can not rob `a0` or `a9` and we have `a2, a3, ..., a8` range to rob
    2. Do not rob house `a0`, then we have `a1, a2, ... a9` range to rob.

    """
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def rob_helper(nums):
            h0, h1 = 0, 0
            for num in nums:
                ans = max(h1, h0 + num)
                h0 = h1
                h1 = ans
            return ans

        ans1 = rob_helper(nums[:len(nums)-1])
        ans2 = rob_helper(nums[1:len(nums)])
        return max(ans1, ans2)


def main():
    s = Solution()
    nums = [2, 3, 2]
    print(f"Input: {nums} \nOutput: {s.rob(nums)}")
    nums = [1, 2, 3, 1]
    print(f"Input: {nums} \nOutput: {s.rob(nums)}")
    nums = [2, 7, 9, 3, 1]
    print(f"Input: {nums} \nOutput: {s.rob(nums)}")


if __name__ == "__main__":
    main()
