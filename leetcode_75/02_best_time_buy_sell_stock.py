"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        a, b = 0, 1
        highest = 0
        while b < len(prices):
            curr_profit = prices[b] - prices[a]
            if curr_profit > 0:
                highest = max(highest, curr_profit)
            else:
                a = b
            b += 1

        return highest


def main():
    prices = [7, 6, 4, 3, 1]
    expected = 0

    solve = Solution()
    ans = solve.maxProfit(prices)
    print(ans, ans == expected)


if __name__ == "__main__":
    main()
