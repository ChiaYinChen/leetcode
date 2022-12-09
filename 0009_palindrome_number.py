"""
0009. Palindrome Number (Easy)
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x < 0 or x = 10
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10
        return x == res or x == res // 10


def main():
    s = Solution()
    x = 121
    print(f"Input: {x} \nOutput: {s.isPalindrome(x)}")
    x = -121
    print(f"Input: {x} \nOutput: {s.isPalindrome(x)}")
    x = 10
    print(f"Input: {x} \nOutput: {s.isPalindrome(x)}")


if __name__ == "__main__":
    main()
