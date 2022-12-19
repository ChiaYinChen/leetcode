"""
0509. Fibonacci Number (Easy)
https://leetcode.com/problems/fibonacci-number/
"""


# O(N) space
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]


# O(1) space
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
#
#         two_back = 0
#         one_back = 1
#         for i in range(2, n+1):
#             curr = one_back + two_back
#             two_back = one_back
#             one_back = curr
#         return curr


def main():
    s = Solution()
    n = 2
    print(f"Input: n={n} \nOutput: {s.fib(n)}")
    n = 3
    print(f"Input: n={n} \nOutput: {s.fib(n)}")
    n = 4
    print(f"Input: n={n} \nOutput: {s.fib(n)}")


if __name__ == "__main__":
    main()
