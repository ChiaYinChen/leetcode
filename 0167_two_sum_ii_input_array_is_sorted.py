"""
0167. Two Sum II - Input Array Is Sorted (Medium)
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            elif total > target:
                right -= 1
        # not found
        return [-1, -1]


def main():
    s = Solution()
    numbers = [2, 7, 11, 15]
    target = 18
    print(f"Input: numbers={numbers}, target={target} \nOutput: {s.twoSum(numbers, target)}")
    numbers = [2, 3, 4]
    target = 8
    print(f"Input: numbers={numbers}, target={target} \nOutput: {s.twoSum(numbers, target)}")
    numbers = [-1, 0]
    target = -1
    print(f"Input: numbers={numbers}, target={target} \nOutput: {s.twoSum(numbers, target)}")


if __name__ == "__main__":
    main()
