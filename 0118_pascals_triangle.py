"""
0118. Pascal's Triangle (Easy)
https://leetcode.com/problems/pascals-triangle/

same as 0119
"""


# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        dp = [[0] * i for i in range(1, numRows + 1)]

        for i in range(numRows):
            dp[i][0] = 1
            dp[i][i] = 1

            if i < 2:
                continue

            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp


def main():
    s = Solution()
    numRows = 5
    print(f"Input: {numRows} \nOutput: {s.generate(numRows)}")
    numRows = 1
    print(f"Input: {numRows} \nOutput: {s.generate(numRows)}")


if __name__ == "__main__":
    main()
