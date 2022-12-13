"""
0344. Reverse String (Easy)
https://leetcode.com/problems/reverse-string/
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


def main():
    s = Solution()
    strs = ["h", "e", "l", "l", "o"]
    print(f"Input: {strs} \nOutput: {s.reverseString(strs)}")
    strs = ["H", "a", "n", "n", "a", "h"]
    print(f"Input: {strs} \nOutput: {s.reverseString(strs)}")


if __name__ == "__main__":
    main()
