"""
0242. Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        # build a hashmap and save count of each char from the string s
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        # iterate over t string and reduce count if the char found in hashmap
        for ch in t:
            if ch not in dic:
                return False
            dic[ch] -= 1
            if dic[ch] < 0:
                return False
        return True


def main():
    s = Solution()
    str1 = "anagram"
    str2 = "nagarma"
    print(f"Input: str1={str1}, str2={str2} \nOutput: {s.isAnagram(str1, str2)}")
    str1 = "rat"
    str2 = "car"
    print(f"Input: str1={str1}, str2={str2} \nOutput: {s.isAnagram(str1, str2)}")


if __name__ == "__main__":
    main()
