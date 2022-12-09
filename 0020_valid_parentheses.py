"""
0020. Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # the brackets appear in pairs, the length of the string should be even
        if len(s) % 2 == 1:
            return False

        stack = []
        for char in s:
            match char:
                case "(" | "{" | "[":
                    stack.append(char)

                case ")" | "}" | "]":
                    if len(stack) == 0:
                        return False

                    top = stack.pop()

                    if char == ")" and top != "(":
                        return False
                    if char == "}" and top != "{":
                        return False
                    if char == "]" and top != "[":
                        return False

                case _:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


def main():
    s = Solution()
    strs = "()"
    print(f"Input: {strs} \nOutput: {s.isValid(strs)}")
    strs = "()[]{}"
    print(f"Input: {strs} \nOutput: {s.isValid(strs)}")
    strs = "[(])"
    print(f"Input: {strs} \nOutput: {s.isValid(strs)}")


if __name__ == "__main__":
    main()
