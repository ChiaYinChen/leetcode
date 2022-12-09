"""
0704. Binary Search (Easy)
https://leetcode.com/problems/binary-search/

same as 0035
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


def main():
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(f"Input: nums={nums}, target={target} \nOutput: {s.search(nums, target)}")
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(f"Input: nums={nums}, target={target} \nOutput: {s.search(nums, target)}")


if __name__ == "__main__":
    main()
