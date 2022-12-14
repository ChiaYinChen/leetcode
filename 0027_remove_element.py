"""
0027. Remove Element (Easy)
https://leetcode.com/problems/remove-element/

same as 0283
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        slow, fast = 0, 0
        while (fast < len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return slow
        # return nums


def main():
    s = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(f"Input: nums={nums}, val={val} \nOutput: {s.removeElement(nums, val)}")
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(f"Input: nums={nums}, val={val} \nOutput: {s.removeElement(nums, val)}")


if __name__ == "__main__":
    main()
