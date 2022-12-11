"""
0026. Remove Duplicates from Sorted Array (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        slow, fast = 0, 1
        while (fast < len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1


def main():
    s = Solution()
    nums = [1, 1, 2]
    print(f"Input: {nums} \nOutput: {s.removeDuplicates(nums)}")
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"Input: {nums} \nOutput: {s.removeDuplicates(nums)}")


if __name__ == "__main__":
    main()
