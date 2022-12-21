"""
0153. Find Minimum in Rotated Sorted Array (Medium)
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]  # or nums[right]


def main():
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    print(f"Input: {nums} \nOutput: {s.findMin(nums)}")
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(f"Input: {nums} \nOutput: {s.findMin(nums)}")
    nums = [11, 13, 15, 17]
    print(f"Input: {nums} \nOutput: {s.findMin(nums)}")


if __name__ == "__main__":
    main()
