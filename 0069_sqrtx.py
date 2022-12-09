"""
0069. Sqrt(x) (Easy)
https://leetcode.com/problems/sqrtx/
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        use binary search to reduce the time complexity

        step
        1. loop over a range 0 ~ x
        2. find the largest result for ans^2 <= x
        """
        left = 0
        right = x
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


def main():
    s = Solution()
    x = 4
    print(f"Input: {x} \nOutput: {s.mySqrt(x)}")
    x = 65
    print(f"Input: {x} \nOutput: {s.mySqrt(x)}")


if __name__ == "__main__":
    main()
