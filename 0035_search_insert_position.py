"""
0035. Search Insert Position (Easy)
https://leetcode.com/problems/search-insert-position/

same as 0704
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:  # if `left == right+1` then break ([right + 1, right])
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


def main():
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    print(f"Input: nums={nums}, target={target} \nOutput: {s.searchInsert(nums, target)}")
    nums = [1, 3, 5, 6]
    target = 2
    print(f"Input: nums={nums}, target={target} \nOutput: {s.searchInsert(nums, target)}")
    nums = [1, 3, 5, 6]
    target = 7
    print(f"Input: nums={nums}, target={target} \nOutput: {s.searchInsert(nums, target)}")
    nums = [1, 2, 3, 3, 3, 3, 5, 6]
    target = 3
    print(f"Input: nums={nums}, target={target} \nOutput: {s.searchInsert(nums, target)}")


if __name__ == "__main__":
    main()
