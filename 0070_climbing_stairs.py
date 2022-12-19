"""
0070. Climbing Stairs (Easy)
https://leetcode.com/problems/climbing-stairs/

same as 0509
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


def main():
    s = Solution()
    n = 2
    print(f"Input: n={n} \nOutput: {s.climbStairs(n)}")
    n = 3
    print(f"Input: n={n} \nOutput: {s.climbStairs(n)}")
    n = 4
    print(f"Input: n={n} \nOutput: {s.climbStairs(n)}")


if __name__ == "__main__":
    main()
