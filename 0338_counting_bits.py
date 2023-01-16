"""
0338. Counting Bits (Easy)
https://leetcode.com/problems/counting-bits/
"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            if i % 2 == 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i // 2]
        return dp


def main():
    s = Solution()
    n = 2
    print(f"Input: {n} \nOutput: {s.countBits(n)}")
    n = 5
    print(f"Input: {n} \nOutput: {s.countBits(n)}")


if __name__ == "__main__":
    main()
