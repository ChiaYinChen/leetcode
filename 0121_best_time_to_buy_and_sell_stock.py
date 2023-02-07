"""
0121. Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


def main():
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Input: {prices} \nOutput: {s.maxProfit(prices)}")
    prices = [7, 6, 4, 3, 1]
    print(f"Input: {prices} \nOutput: {s.maxProfit(prices)}")


if __name__ == "__main__":
    main()
