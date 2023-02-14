"""
0168. Excel Sheet Column Title (Easy)
https://leetcode.com/problems/excel-sheet-column-title/
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a_z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""
        while columnNumber:
            columnNumber -= 1
            ans = a_z[columnNumber % 26] + ans
            columnNumber = columnNumber // 26
        return ans


def main():
    s = Solution()
    num = 1
    print(f"Input: {num} \nOutput: {s.convertToTitle(num)}")
    num = 28
    print(f"Input: {num} \nOutput: {s.convertToTitle(num)}")
    num = 701
    print(f"Input: {num} \nOutput: {s.convertToTitle(num)}")


if __name__ == "__main__":
    main()
