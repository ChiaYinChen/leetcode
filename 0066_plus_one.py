"""
0066. Plus One (Easy)
https://leetcode.com/problems/plus-one/
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits = [0] + digits  # for digit = [9], [9,9], [9,9,9], etc.
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] != 10:
                break
            else:
                digits[i] = 0
                digits[i-1] += 1

        if digits[0] == 0:
            return digits[1:]
        else:
            return digits


def main():
    s = Solution()
    digits = [1, 2, 3]
    print(f"Input: {digits} \nOutput: {s.plusOne(digits)}")
    digits = [9, 9]
    print(f"Input: {digits} \nOutput: {s.plusOne(digits)}")


if __name__ == "__main__":
    main()
