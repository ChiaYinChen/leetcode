"""
0080. Remove Duplicates from Sorted Array II (Medium)
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        size = len(nums)
        if size <= 2:
            return size
        slow, fast = 2, 2
        while (fast < size):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


def main():
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print(f"Input: {nums} \nOutput: {s.removeDuplicates(nums)}")
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(f"Input: {nums} \nOutput: {s.removeDuplicates(nums)}")


if __name__ == "__main__":
    main()
