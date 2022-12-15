"""
0155. Min Stack (Medium)
https://leetcode.com/problems/min-stack/
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.min = x


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        node = Node(val)
        if not self.stack:
            self.stack.append(node)
        else:
            top_node = self.stack[-1]
            if node.min > top_node.min:
                node.min = top_node.min
            self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min


def main():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())


if __name__ == "__main__":
    main()
