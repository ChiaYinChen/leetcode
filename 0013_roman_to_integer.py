"""
0013. Roman to Integer (Easy)
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0
        for i in range(len(s)):
            if i < (len(s)-1) and numbers[s[i]] < numbers[s[i+1]]:
                ans -= numbers[s[i]]
            else:
                ans += numbers[s[i]]
        return ans


def main():
    s = Solution()
    strs = "III"
    print(f"Input: {strs} \nOutput: {s.romanToInt(strs)}")
    strs = "LVIII"
    print(f"Input: {strs} \nOutput: {s.romanToInt(strs)}")
    strs = "MCMXCIV"
    print(f"Input: {strs} \nOutput: {s.romanToInt(strs)}")


if __name__ == "__main__":
    main()
