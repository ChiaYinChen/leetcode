"""
0171. Excel Sheet Column Number (Easy)
https://leetcode.com/problems/excel-sheet-column-number/
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        a_z = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = 0
        for i in range(len(columnTitle)):
            ans *= 26
            ans += a_z.index(columnTitle[i])
        return ans


def main():
    s = Solution()
    strs = "A"
    print(f"Input: {strs} \nOutput: {s.titleToNumber(strs)}")
    strs = "AB"
    print(f"Input: {strs} \nOutput: {s.titleToNumber(strs)}")
    strs = "ZY"
    print(f"Input: {strs} \nOutput: {s.titleToNumber(strs)}")


if __name__ == "__main__":
    main()
