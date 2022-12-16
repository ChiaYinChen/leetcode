"""
0227. Basic Calculator II (Medium)
https://leetcode.com/problems/basic-calculator-ii/
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = "+"
        index = 0
        while index < len(s):
            char = s[index]
            if char.isdigit():
                start = index
                while index < len(s) and s[index].isdigit():
                    index += 1
                curr_num = int(s[start:index])
                if op == "+":
                    stack.append(curr_num)
                elif op == "-":
                    stack.append(-curr_num)
                elif op == "*":
                    top = stack.pop()
                    stack.append(top * curr_num)
                elif op == "/":
                    top = stack.pop()
                    stack.append(int(top / curr_num))
            elif char in "+-*/":
                op = char
                index += 1
            else:
                index += 1  # char = " "

        return sum(stack)


def main():
    s = Solution()
    strs = "3+2*2"
    print(f"Input: {strs} \nOutput: {s.calculate(strs)}")
    strs = " 3/2 "
    print(f"Input: {strs} \nOutput: {s.calculate(strs)}")
    strs = " 3+5 / 2 "
    print(f"Input: {strs} \nOutput: {s.calculate(strs)}")


if __name__ == "__main__":
    main()
