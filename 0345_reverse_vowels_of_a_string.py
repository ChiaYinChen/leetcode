"""
0345. Reverse Vowels of a String (Easy)
https://leetcode.com/problems/reverse-vowels-of-a-string/
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        left = 0
        right = len(s)-1
        s_list = list(s)
        while left < right:
            if s_list[left] not in vowels:
                left += 1
                continue
            if s_list[right] not in vowels:
                right -= 1
                continue
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return "".join(s_list)


def main():
    s = Solution()
    strs = "hello"
    print(f"Input: {strs} \nOutput: {s.reverseVowels(strs)}")
    strs = "leetcode"
    print(f"Input: {strs} \nOutput: {s.reverseVowels(strs)}")


if __name__ == "__main__":
    main()
