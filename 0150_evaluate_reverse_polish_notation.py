"""
0150. Evaluate Reverse Polish Notation (Medium)
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(-stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                stack.append(int(1 / stack.pop() * stack.pop()))
            else:
                stack.append(int(token))
        return stack.pop()


def main():
    s = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    print(f"Input: {tokens} \nOutput: {s.evalRPN(tokens)}")
    tokens = ["4", "13", "5", "/", "+"]
    print(f"Input: {tokens} \nOutput: {s.evalRPN(tokens)}")
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(f"Input: {tokens} \nOutput: {s.evalRPN(tokens)}")


if __name__ == "__main__":
    main()
