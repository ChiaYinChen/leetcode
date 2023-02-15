"""
0205. Isomorphic Strings (Easy)
https://leetcode.com/problems/isomorphic-strings/
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = dict()
        t_map = dict()
        for i in range(len(s)):
            if s[i] in s_map and s_map[s[i]] != t[i]:
                return False
            if t[i] in t_map and t_map[t[i]] != s[i]:
                return False
            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]
        return True


def main():
    s = Solution()
    str1 = "egg"
    str2 = "add"
    print(f"Input: str1={str1}, str2={str2} \nOutput: {s.isIsomorphic(str1, str2)}")
    str1 = "foo"
    str2 = "bar"
    print(f"Input: str1={str1}, str2={str2} \nOutput: {s.isIsomorphic(str1, str2)}")
    str1 = "paper"
    str2 = "title"
    print(f"Input: str1={str1}, str2={str2} \nOutput: {s.isIsomorphic(str1, str2)}")


if __name__ == "__main__":
    main()
