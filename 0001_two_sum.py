"""
0001. Two Sum (Easy)
https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # initialize a dictionary (Hashmap)
        dic = {}
        for i, num in enumerate(nums):
            if (target - num) in dic:
                return [dic.get(target - num), i]

            # store key and value in reverse to find index from element in array
            dic[num] = i


def main():
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: nums={nums}, target={target} \nOutput: {s.twoSum(nums, target)}")
    nums = [3, 2, 4]
    target = 6
    print(f"Input: nums={nums}, target={target} \nOutput: {s.twoSum(nums, target)}")
    nums = [3, 3]
    target = 6
    print(f"Input: nums={nums}, target={target} \nOutput: {s.twoSum(nums, target)}")


if __name__ == "__main__":
    main()
