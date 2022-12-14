"""
0283. Move Zeroes (Easy)
https://leetcode.com/problems/move-zeroes/

same as 0027
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while (fast < len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums


def main():
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    print(f"Input: {nums} \nOutput: {s.moveZeroes(nums)}")
    nums = [0]
    print(f"Input: {nums} \nOutput: {s.moveZeroes(nums)}")


if __name__ == "__main__":
    main()
