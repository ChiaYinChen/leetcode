"""
1137. N-th Tribonacci Number (Easy)
https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1

        t0, t1, t2 = 0, 1, 1
        for i in range(3, n+1):
            ans = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = ans
        return ans


def main():
    s = Solution()
    n = 4
    print(f"Input: {n} \nOutput: {s.tribonacci(n)}")
    n = 25
    print(f"Input: {n} \nOutput: {s.tribonacci(n)}")


if __name__ == "__main__":
    main()
