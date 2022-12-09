"""
0014. Longest Common Prefix (Easy)
https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""  # empty strs

        if len(strs) == 1:
            return strs[0]

        # sort strings by length and alphabetical
        # ref: https://stackoverflow.com/a/4659539
        strs.sort(key=lambda x: (len(x), x))

        # compare the first two strings
        for i, char in enumerate(strs[0]):
            if char != strs[1][i]:
                common = strs[1][:i]
                if len(common) == 0:
                    return ""  # first two strings do not have common prefix
                break
        else:
            common = strs[0]  # first two strings are same

        for i in range(2, len(strs)):
            while common != strs[i][:len(common)]:
                common = common[:-1]  # reduce common prefix from the end
                if len(common) == 0:
                    return ""  # current common prefix is empty
        return common


def main():
    s = Solution()
    strs = ["flower", "flow", "flight"]
    print(f"Input: {strs} \nOutput: {s.longestCommonPrefix(strs)}")
    strs = ["dog", "racecar", "car"]
    print(f"Input: {strs} \nOutput: {s.longestCommonPrefix(strs)}")


if __name__ == "__main__":
    main()
