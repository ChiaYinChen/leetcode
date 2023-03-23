"""
0058. Length of Last Word (Easy)
https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if ans == 0:
                    continue
                return ans
            else:
                ans += 1
        return ans


def main():
    s = Solution()
    strs = "Hello World"
    print(f"Input: {strs} \nOutput: {s.lengthOfLastWord(strs)}")
    strs = "   fly me   to   the moon  "
    print(f"Input: {strs} \nOutput: {s.lengthOfLastWord(strs)}")
    strs = "luffy is still joyboy"
    print(f"Input: {strs} \nOutput: {s.lengthOfLastWord(strs)}")


if __name__ == "__main__":
    main()
