"""
0062. Unique Paths (Medium)
https://leetcode.com/problems/unique-paths/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][0] = 1
                    dp[0][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


def main():
    s = Solution()
    m = 3
    n = 7
    print(f"Input: m={m}, n={n} \nOutput: {s.uniquePaths(m, n)}")
    m = 3
    n = 2
    print(f"Input: m={m}, n={n} \nOutput: {s.uniquePaths(m, n)}")


if __name__ == "__main__":
    main()
