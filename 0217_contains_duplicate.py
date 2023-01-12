"""
0217. Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = num
        return False


def main():
    s = Solution()
    nums = [1, 2, 3, 1]
    print(f"Input: {nums} \nOutput: {s.containsDuplicate(nums)}")
    nums = [1, 2, 3, 4]
    print(f"Input: {nums} \nOutput: {s.containsDuplicate(nums)}")
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: {nums} \nOutput: {s.containsDuplicate(nums)}")


if __name__ == "__main__":
    main()
