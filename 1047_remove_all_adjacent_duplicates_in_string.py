"""
1047. Remove All Adjacent Duplicates In String (Easy)
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in list(s):
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


def main():
    s = Solution()
    strs = "abbaca"
    print(f"Input: {strs} \nOutput: {s.removeDuplicates(strs)}")
    strs = "azxxzy"
    print(f"Input: {strs} \nOutput: {s.removeDuplicates(strs)}")


if __name__ == "__main__":
    main()
