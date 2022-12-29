"""
0119. Pascal's Triangle II (Easy)
https://leetcode.com/problems/pascals-triangle-ii/

same as 0118
"""


# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        numRows = rowIndex + 1
        dp = [1 for _ in range(numRows)]

        for i in range(numRows):
            if i < 2:
                continue
            for j in range(i - 1, 0, -1):
                dp[j] = dp[j - 1] + dp[j]

        return dp


def main():
    s = Solution()
    numRows = 3
    print(f"Input: {numRows} \nOutput: {s.getRow(numRows)}")
    numRows = 0
    print(f"Input: {numRows} \nOutput: {s.getRow(numRows)}")


if __name__ == "__main__":
    main()
