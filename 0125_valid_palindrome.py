"""
0125. Valid Palindrome (Easy)
https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True


def main():
    s = Solution()
    strs = "A man, a plan, a canal: Panama"
    print(f"Input: {strs} \nOutput: {s.isPalindrome(strs)}")
    strs = "race a car"
    print(f"Input: {strs} \nOutput: {s.isPalindrome(strs)}")
    strs = " "
    print(f"Input: {strs} \nOutput: {s.isPalindrome(strs)}")


if __name__ == "__main__":
    main()
