"""
0011. Container With Most Water (Medium)
https://leetcode.com/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return ans


def main():
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Input: {height} \nOutput: {s.maxArea(height)}")
    height = [1, 1]
    print(f"Input: {height} \nOutput: {s.maxArea(height)}")


if __name__ == "__main__":
    main()
