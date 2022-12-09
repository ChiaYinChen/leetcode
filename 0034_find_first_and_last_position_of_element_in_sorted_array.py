"""
0034. Find First and Last Position of Element in Sorted Array (Medium)
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        require: must write an algorithm with O(log n) runtime complexity.

        進行兩次 binary search
        第一次盡量向左搜尋
        第二次盡量向右搜尋
        """
        ans = [-1, -1]
        if len(nums) == 0:
            return ans

        left, right = 0, len(nums) - 1
        while left < right:  # if `left == right` then break ([right, right])
            mid = (left + right) // 2  # the number on the left in the middle
            if nums[mid] < target:  # search in [mid + 1, right]
                left = mid + 1
            elif nums[mid] >= target:  # search in [left, mid]
                right = mid

        if nums[left] != target:  # same as `nums[right] != target`
            return ans

        ans[0] = left

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2  # the number on the right in the middle
            if nums[mid] > target:  # search in [left, mid -1]
                right = mid - 1
            elif nums[mid] <= target:  # search in [mid, right]
                left = mid

        if nums[left] == target:
            ans[1] = left

        return ans


def main():
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(f"Input: nums={nums}, target={target} \nOutput: {s.searchRange(nums, target)}")
    nums = [5, 7, 8, 8, 10]
    target = 7
    print(f"Input: nums={nums}, target={target} \nOutput: {s.searchRange(nums, target)}")
    nums = [5, 7, 8, 8, 10]
    target = 16
    print(f"Input: nums={nums}, target={target} \nOutput: {s.searchRange(nums, target)}")
    nums = []
    target = 16
    print(f"Input: nums={nums}, target={target} \nOutput: {s.searchRange(nums, target)}")


if __name__ == "__main__":
    main()
