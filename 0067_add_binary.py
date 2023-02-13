"""
0067. Add Binary(Easy)
https://leetcode.com/problems/add-binary/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or carry:
            # Add the corresponding digits and carry value
            carry += int(a[i]) if i >= 0 else 0
            carry += int(b[j]) if j >= 0 else 0
            # Get the current digit of the result
            ans = str(carry % 2) + ans
            # Update the carry value
            carry = carry // 2
            i -= 1
            j -= 1
        return ans


def main():
    s = Solution()
    a = "11"
    b = "1"
    print(f"Input: a={a}, b={b} \nOutput: {s.addBinary(a, b)}")
    a = "1001"
    b = "11"
    print(f"Input: a={a}, b={b} \nOutput: {s.addBinary(a, b)}")
    a = "1010"
    b = "1011"
    print(f"Input: a={a}, b={b} \nOutput: {s.addBinary(a, b)}")


if __name__ == "__main__":
    main()
